import socket
import time
import sys
import random # import randint

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


host = "192.168.0.100" # socket.gethostname()
port = 6012  # socket server port number
veh_socket = socket.socket()  # instantiate
print ("tring to conct ...")
flag = 0

while flag == 0 :
    try : 
        veh_socket.connect((host, port))  # connect to the server
        flag = 1
    except :
        print ("Failed ... Trying to connect again")

print ("Connection successful")

auth_init_r = random.randint(2, 1000)

print ("HPw is ", sys.argv[1]) # NVID
print ("NVID is ", sys.argv[2]) # HPW
#print ("p(x) is ", sys.argv[3]) # p(x)
#print ("h(x) is ", sys.argv[4]) # h(x)

send1 = str(auth_init_r) + "&"+ sys.argv[1] + "&"+ sys.argv[2]+ "&02A" # rand r, NVID, HPW, Auth req
start_time = time.time()

n = 103
h_s = [int(i) for i in sys.argv[4].split(',')]  
poly_s = [int(i) for i in sys.argv[3].split(',')]   # [1, -3, 2, 0] # [4, 9, 5, 4]

print ("h(x) is ", h_s)
print ("p(x) is ", poly_s)

veh_socket.send(send1.encode('utf')) # send r, HPW, NVID, Auth req to RSU_i

recv1 = veh_socket.recv(1024).decode() # recvd prover key
values = [str(i) for i in recv1.split('&')]
print ("values are ", values)

if values[0] == str(auth_init_r) :
    print("random num matched ...")

    g_s_i_val = [int(i) for i in values[1].split(',')] 
    g_alpha_s_i_val = [int(i) for i in values[2].split(',')]

    g_s_i_val_temp = g_s_i_val.copy()

    #print ("g_s_i_val bfr rev is ", g_s_i_val)
    #print ("g_alpha_s_i_val bfr rev is ", g_alpha_s_i_val)

    g_s_i_val.reverse()
    g_alpha_s_i_val.reverse()

    h_s.reverse()

    #print ("g_s_i_val after rev is ", g_s_i_val)
    #print ("g_alpha_s_i_val after rev is ", g_alpha_s_i_val)

    g_p_s_val = 1
    g_alpha_p_val = 1
    g_h_s = 1

    print ("poly_s is ", poly_s)
    print ("g_alpha_s_i_val is ", g_alpha_s_i_val)
    for i in range(len(poly_s)):
        print("For g_p_s ", g_s_i_val[i], poly_s[i])
        print ("for alpha DOing mod on ", g_alpha_s_i_val[i], poly_s[i])
        g_p_s_val *= int(pow(g_s_i_val[i], poly_s[i], n))
    
        g_alpha_p_val *= int(pow(g_alpha_s_i_val[i], poly_s[i], n))
        print ("--g_alpha_p_s_val is ", g_alpha_p_val)
        g_p_s_val = g_p_s_val % n
        g_alpha_p_val = g_alpha_p_val % n


    print ("g_s_i_val_temp is ", g_s_i_val_temp)
    print ("\n")

    for i in range(len(h_s)):
        print ("hs[i] is ", h_s[i])
        print ("g_s_i_val_temp[i] is ", g_s_i_val_temp[i])
        if h_s[i] != 0:
            g_h_s *= int(pow(g_s_i_val_temp[i], h_s[i], n))

    g_h_s_val = g_h_s % n    


    print ("g_h_s is ", g_h_s_val)
    print ("g_p_s is ", g_p_s_val)
    print ("g_alpha_p_val is ", g_alpha_p_val)

    delta = 7 # random.randint(3, 100) # 7

    g_delta_p = int(pow(g_p_s_val, delta, n))
    g_delta_h_s = int(pow(g_h_s_val, delta, n))
    g_delta_alpha_p = int(pow(g_alpha_p_val, delta, n))

    print("proof pi is ", g_delta_p, g_delta_h_s, g_delta_alpha_p)
    proof = [g_delta_p, g_delta_h_s, g_delta_alpha_p]


    proof1 = listToString(proof)
    send_nvid_proof = str(sys.argv[2])+ "&"+ str(auth_init_r)+ "&"+ proof1
    print("proof pi is ", proof1)

    veh_socket.send(send_nvid_proof.encode('utf')) # sending proof to RSU

    recv2 = veh_socket.recv(1024).decode()  # recv session key and new VID
    recv2 = [str(i) for i in recv2.split('&')]

    print ("Recvd Session key is ", recv2[0])
    print ("Recvd r is ", recv2[1])
    print ("Recvd new VID is ", recv2[2])

    end_time = time.time()
    print ("Total time for auth is ", end_time - start_time ," sec")

    veh_socket.close() 



