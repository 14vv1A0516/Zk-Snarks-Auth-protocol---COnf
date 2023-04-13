import socket
import time
import sys
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from base64 import b64encode, b64decode
import hashlib
import ast

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

print ("Details of veh is ", sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]) # session key, r, VID, Hand_req
send1 = encrypt (sys.argv[3]+ "&"+ sys.argv[2], sys.argv[1] ) # Data: VID, rand r and password: session key
print ("Sending Enc data is ", send1," and type is ", type(send1))
print ("Dec text is ", decrypt(send1, sys.argv[1]))

host = "192.168.1.100" # socket.gethostname()
port = 6017  # socket server port number
veh_socket = socket.socket()  # instantiate
flag = 0

while flag == 0 :
    try : 
        veh_socket.connect((host, port))  # connect to the server
        flag = 1
    except :
        print ("Failed ... Trying to connect again")

print ("conn with RSU j done ----------")

send1 = str(send1) + '$$' + sys.argv[3]+ "$$"+ sys.argv[4] # enc, VID, Hand req

print ("Sending Enc: ", send1, " VID: ", sys.argv[3], "Hand_req: ", sys.argv[4])

# msg = sys.argv[1] + ","+ sys.argv[2] +","+ sys.argv[3] # Session key, r, vid, hand_req
start_time = time.time()
veh_socket.send(send1.encode('utf')) # send enc

hand_res = veh_socket.recv(1024).decode() # enc, vid
# print ("Recvd key after hand auth is ", hand_res)
hand_res = [str(i) for i in hand_res.split('&')] 

if hand_res[1] == sys.argv[3] :
   print ("VIDs matched")
   enc_val = ast.literal_eval(hand_res[0]) # str to dict conversion
   dec_key = decrypt(enc_val, sys.argv[1]) # enc and VID
   print ("dec rand no is ", dec_key)
end_time  = time.time()
print ("Total time for handover auth is ", end_time-start_time, "sec" )

veh_socket.close()

