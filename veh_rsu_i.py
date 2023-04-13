import string
import socket
import random # import randint
import time 
import threading 
from base64 import b64encode, b64decode
import hashlib
import pyexcel as pe
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from collections import OrderedDict 

def encrypt(plain_text, password):
    # generate a random salt
    salt = get_random_bytes(AES.block_size)

    # use the Scrypt KDF to get a private key from the password
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    # create cipher config
    cipher_config = AES.new(private_key, AES.MODE_GCM)

    # return a dictionary with the encrypted text
    cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
    return {
        'cipher_text': b64encode(cipher_text).decode('utf-8'),
        'salt': b64encode(salt).decode('utf-8'),
        'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
        'tag': b64encode(tag).decode('utf-8')
    }


def decrypt(enc_dict, password):
    # decode the dictionary entries from base64
    salt = b64decode(enc_dict['salt'])
    cipher_text = b64decode(enc_dict['cipher_text'])
    nonce = b64decode(enc_dict['nonce'])
    tag = b64decode(enc_dict['tag'])
    

    # generate the private key from the password and salt
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    # create the cipher config
    cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

    # decrypt the cipher text
    decrypted = cipher.decrypt_and_verify(cipher_text, tag)

    return decrypted

def listToString(s):
 
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in s:
        str1 += str(ele)
        str1 += ","
    str1 = str1[:len(str1)-1]
    print ("str returning is ", str1)
    # return string
    return str1

def horner(poly, n, x): # poly list(coeff), len(poly), x value to substitute
 
    # Initialize result
    result = poly[0]
 
    # Evaluate value of polynomial
    # using Horner's method
    for i in range(1, n):
 
        result = result*x + poly[i]
 
    return result

def handle_rsu_j(rsuj_socket) :
    while(1) :
        print ("Conn with RSU j done ...")
        veh_keys = rsuj_socket.recv(1024).decode() # key, x, VID
        print ("Recd veh keys from RSU_j is ", veh_keys)
        sheet = pe.get_sheet(file_name="rsu_auth_sheet_i.xlsx")
        
        sheet.row += [str(i) for i in veh_keys.split('&')]
        sheet.save_as ("rsu_auth_sheet_i.xlsx")

def handle_client_veh(client_socket, client_address, rsuj_socket) : 
    n = 103
    N = 7 # size of VID

    auth_req = client_socket.recv(1024).decode()  # receive auth_req
    values = [str(i) for i in auth_req.split('&')] # Send NVID, HPW, p(x), h(x) for auth
    print ("values are ", values)

    if values[3] == '02A' :
        print ("Received Authentication request ")
        sheet = pe.get_sheet(file_name="veh_reg_details.xlsx")
        for row in sheet :
            #print ("row is ", row)
            if row[0] == values[1] : # matching NVID                                                                                                                                                                                                                                                                                                                                                                                
                break
        print ("Matched with row ", row) # Matched with row

        if row[5] == values[2] : # compare HPW
            send1 = values[0]+ "&"+  row[4] # r and (g_s_i & g_alpha_s_i)
            alpha = int(row[2])

            client_socket.send(send1.encode())  # sending r, and prove key

            proof = client_socket.recv(1024).decode() # recv NVID, r, proof pi 

            #print ("Proof recvd from Veh is ", proof)

            proof_nvid_r = [str(i) for i in proof.split('&')]
            
            ods_data = OrderedDict()

            #print ("proof recvd is ", proof_nvid_r) # (g^p, g^h, g^p')
            proof = [int(i) for i in proof_nvid_r[2].split(',')]

            print ("----" , int(pow(proof[0], alpha, n)))
            print ("proof [2] is ", proof[2])

            if proof[2] == int(pow(proof[0], alpha, n)): # e(g^p', g) = e(g^p, g^alpha)
                print (" ----- First proof successful")
                tx_val_on_s = int(row[3])
                # print ("g_t_s_val finally is ", g_t_s_val)
                print ("tx_val_on_s on s is ", tx_val_on_s)
                final_res = int(pow(proof[1], tx_val_on_s, n)) # (g_h * g_t_s_val) % n
                print ("final res is ", final_res)
                print ("--- proof[0] is ", proof[0])
                if proof[0] == final_res:
                    print ("---- Second proof successful")
                    
                    veh_id = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))
                    auth_r = random.randint(2000, 10000)
                    session_key = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))
                    print("Gen veh_id is ", veh_id)
                    print("Gen auth_r ", auth_r)
                    print("Gen session_key is ", session_key)
                    sesn_key_vid = session_key+ "&"+ str(auth_r)+ "&"+ veh_id 

                    client_socket.send(sesn_key_vid.encode())
                    rsuj_socket.send(sesn_key_vid.encode())
                    print ("Sent veh key ", sesn_key_vid," to RSU j")
                    print ("===========+++++++++ Auth Done ++++++++++===============\n\n")

                else :
                    print ("Second proof invalid")
                
            else :
                print ("First proof invalid")
    client_socket.close()
            
host_j = "192.168.1.100" # socket.gethostname()
port_j = 8010  # RSU_j connection & initiate port no above 1024
rsuj_socket = socket.socket()  # get instance
rsuj_socket.connect((host_j, port_j))  # connect to the RSU_j
print ("Had conn with RSU j")

host = "192.168.0.100" # socket.gethostname()
print("RSU IP is ", host)
print ("-------------------")
port = 6012  # initiate port no above 1024
server_socket = socket.socket()  # get instance
server_socket.bind((host, port))  # bind host address and port together for veh comm
server_socket.listen(4) 
print ("Had conn with Veh skt")

i = 0
rsu_j = 0

while True :
    print ("For loop i = ", i)
    print ("rsu j is ", rsu_j)

    if rsu_j == 0:
        print ("Thread for RSU j started ...")
        client_thread1 = threading.Thread (target=handle_rsu_j, args= (rsuj_socket,))
        client_thread1.start()
        rsu_j = 1

    print ("Veh trying to connect ...")
    veh_conn, client_address = server_socket.accept()
    print ("\nRecvd conn from veh ", veh_conn, client_address) 

    client_thread2 = threading.Thread (target=handle_client_veh, args= (veh_conn, client_address, rsuj_socket)) #, rsuj_socket))
    client_thread2.start()

    i = i + 1