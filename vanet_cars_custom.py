from mininet.log import setLogLevel, info
import time, sys
from mn_wifi.link import wmediumd
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi
from mn_wifi.wmediumdConnector import interference
from mininet.term import makeTerm 

def topology(args):
    print ("args are ", args)
    'Create a network.'
    net = Mininet_wifi(link=wmediumd, wmediumd_mode=interference)

    info("*** Creating nodes\n")
    if '-m' in args:
        sta1 = net.addStation('sta1', mac='00:00:00:00:00:01', ip='192.168.0.1/24', min_v=1.0, max_v=1.7)
    else:
        sta1 = net.addStation('sta1', mac='00:00:00:00:00:01', ip='192.168.0.1/24', position='1,60,0', min_v=1.0, max_v=1.0, range=3)

    sta2 = net.addStation('sta2', mac='00:00:00:00:00:02', ip='192.168.0.2/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    
    sta3 = net.addStation('sta3', mac='00:00:00:00:00:03', ip='192.168.0.3/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    sta4 = net.addStation('sta4', mac='00:00:00:00:00:04', ip='192.168.0.4/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    sta5 = net.addStation('sta5', mac='00:00:00:00:00:05', ip='192.168.0.5/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    
    sta6 = net.addStation('sta6', mac='00:00:00:00:00:06', ip='192.168.0.6/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    sta7 = net.addStation('sta7', mac='00:00:00:00:00:07', ip='192.168.0.7/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    sta8 = net.addStation('sta8', mac='00:00:00:00:00:08', ip='192.168.0.8/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    sta9 = net.addStation('sta9', mac='00:00:00:00:00:09', ip='192.168.0.9/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    sta10 = net.addStation('sta10', mac='00:00:00:00:00:10', ip='192.168.0.10/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    
    sta11 = net.addStation('sta11', mac='00:00:00:00:00:11', ip='192.168.0.11/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    sta12 = net.addStation('sta12', mac='00:00:00:00:00:12', ip='192.168.0.12/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    sta13 = net.addStation('sta13', mac='00:00:00:00:00:13', ip='192.168.0.13/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    sta14 = net.addStation('sta14', mac='00:00:00:00:00:14', ip='192.168.0.14/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    sta15 = net.addStation('sta15', mac='00:00:00:00:00:15', ip='192.168.0.15/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    
    sta16 = net.addStation('sta16', mac='00:00:00:00:00:16', ip='192.168.0.16/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    sta17 = net.addStation('sta17', mac='00:00:00:00:00:17', ip='192.168.0.17/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    sta18 = net.addStation('sta18', mac='00:00:00:00:00:18', ip='192.168.0.18/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    sta19 = net.addStation('sta19', mac='00:00:00:00:00:19', ip='192.168.0.19/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    sta20 = net.addStation('sta20', mac='00:00:00:00:00:20', ip='192.168.0.20/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    
    sta21 = net.addStation('sta21', mac='00:00:00:00:00:21', ip='192.168.0.21/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    sta22 = net.addStation('sta22', mac='00:00:00:00:00:22', ip='192.168.0.22/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    sta23 = net.addStation('sta23', mac='00:00:00:00:00:23', ip='192.168.0.23/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    sta24 = net.addStation('sta24', mac='00:00:00:00:00:24', ip='192.168.0.24/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    sta25 = net.addStation('sta25', mac='00:00:00:00:00:25', ip='192.168.0.25/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    
    sta26 = net.addStation('sta26', mac='00:00:00:00:00:26', ip='192.168.0.26/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    sta27 = net.addStation('sta27', mac='00:00:00:00:00:27', ip='192.168.0.27/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    sta28 = net.addStation('sta28', mac='00:00:00:00:00:28', ip='192.168.0.28/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    sta29 = net.addStation('sta29', mac='00:00:00:00:00:29', ip='192.168.0.29/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    sta30 = net.addStation('sta30', mac='00:00:00:00:00:30', ip='192.168.0.30/24', position='90,60,0', min_v=1.0, max_v=1.0, range=5)
    
    ap1 = net.addStation('ap1', mac='02:00:00:00:01:00', ip='192.168.0.100/24', position='35,35,0')
    ap2 = net.addStation('ap2', mac='02:00:00:00:02:00', ip='192.168.1.100/24', position='85,35,0')

    net.setPropagationModel(model="logDistance", exp=4.5)

    info("*** Configuring nodes\n")
    net.configureWifiNodes()

    ap1.setMasterMode(intf='ap1-wlan0', ssid='ap1-ssid', channel='4', mode='g', range=30)
    ap2.setMasterMode(intf='ap2-wlan0', ssid='ap2-ssid', channel='4', mode='g', range=30)

    info("*** Adding Link\n")
    net.addLink(ap1, ap2)  # wired connection

    if '-p' not in args:
        info("*** Plotting Graph\n")
        net.plotGraph(max_x=135, max_y=70)

    if '-m' not in args:
        print ("Starting Mobility")
        net.startMobility (time=0, seed=1, model='RandomDirection') #, AC='ssf')

        net.mobility(sta1, 'start', time=4, position='2,35,0')
        net.mobility(sta1, 'stop', time=60, position='120,35,0')

        net.mobility(sta2, 'start', time=8, position='2,35,0')
        net.mobility(sta2, 'stop', time=64, position='120,35,0')
        
        net.mobility(sta3, 'start', time=12, position='2,35,0')
        net.mobility(sta3, 'stop', time=68, position='120,35,0')

        net.mobility(sta4, 'start', time=16, position='2,35,0')
        net.mobility(sta4, 'stop', time=72, position='120,35,0')

        net.mobility(sta5, 'start', time=20, position='2,35,0')
        net.mobility(sta5, 'stop', time=76, position='120,35,0')
        
        net.mobility(sta6, 'start', time=24, position='2,35,0')
        net.mobility(sta6, 'stop', time=80, position='120,35,0')

        net.mobility(sta7, 'start', time=28, position='2,35,0')
        net.mobility(sta7, 'stop', time=84, position='120,35,0')

        net.mobility(sta8, 'start', time=32, position='2,35,0')
        net.mobility(sta8, 'stop', time=88, position='120,35,0')

        net.mobility(sta9, 'start', time=36, position='2,35,0')
        net.mobility(sta9, 'stop', time=92, position='120,35,0')

        net.mobility(sta10, 'start', time=40, position='2,35,0')
        net.mobility(sta10, 'stop', time=96, position='120,35,0')
        
        net.mobility(sta11, 'start', time=44, position='2,35,0')
        net.mobility(sta11, 'stop', time=100, position='120,35,0')

        net.mobility(sta12, 'start', time=48, position='2,35,0')
        net.mobility(sta12, 'stop', time=104, position='120,35,0')

        net.mobility(sta13, 'start', time=52, position='2,35,0')
        net.mobility(sta13, 'stop', time=108, position='120,35,0')

        net.mobility(sta14, 'start', time=56, position='2,35,0')
        net.mobility(sta14, 'stop', time=112, position='120,35,0')

        net.mobility(sta15, 'start', time=60, position='2,35,0')
        net.mobility(sta15, 'stop', time=116, position='120,35,0')
        
        net.mobility(sta16, 'start', time=64, position='2,35,0')
        net.mobility(sta16, 'stop', time=120, position='120,35,0')

        net.mobility(sta17, 'start', time=68, position='2,35,0')
        net.mobility(sta17, 'stop', time=124, position='120,35,0')

        net.mobility(sta18, 'start', time=72, position='25,35,0')
        net.mobility(sta18, 'stop', time=128, position='120,35,0')

        net.mobility(sta19, 'start', time=76, position='2,35,0')
        net.mobility(sta19, 'stop', time=132, position='120,35,0')

        net.mobility(sta20, 'start', time=80, position='2,35,0')
        net.mobility(sta20, 'stop', time=136, position='120,35,0')
        
        net.mobility(sta21, 'start', time=84, position='2,35,0')
        net.mobility(sta21, 'stop', time=140, position='120,35,0')

        net.mobility(sta22, 'start', time=88, position='2,35,0')
        net.mobility(sta22, 'stop', time=144, position='120,35,0')

        net.mobility(sta23, 'start', time=92, position='2,35,0')
        net.mobility(sta23, 'stop', time=148, position='120,35,0')

        net.mobility(sta24, 'start', time=96, position='2,35,0')
        net.mobility(sta24, 'stop', time=152, position='120,35,0')

        net.mobility(sta25, 'start', time=100, position='2,35,0')
        net.mobility(sta25, 'stop', time=156, position='120,35,0')
        
        net.mobility(sta26, 'start', time=104, position='2,35,0')
        net.mobility(sta26, 'stop', time=160, position='120,35,0')

        net.mobility(sta27, 'start', time=108, position='2,35,0')
        net.mobility(sta27, 'stop', time=164, position='120,35,0')

        net.mobility(sta28, 'start', time=112, position='2,35,0')
        net.mobility(sta28, 'stop', time=168, position='120,35,0')

        net.mobility(sta29, 'start', time=116, position='2,35,0')
        net.mobility(sta29, 'stop', time=172, position='120,35,0')

        net.mobility(sta30, 'start', time=120, position='2,35,0')
        net.mobility(sta30, 'stop', time=176, position='120,35,0')
        
        net.stopMobility (time=200)

    info("*** Starting network\n")
    net.build()

    ap1.cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')
    ap2.cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')

    ap1.setIP('192.168.0.100/24', intf='ap1-wlan0')
    ap1.setIP('192.168.2.1/24', intf='ap1-eth1')
    ap2.setIP('192.168.1.100/24', intf='ap2-wlan0')
    ap2.setIP('192.168.2.2/24', intf='ap2-eth1')

    ap1.cmd('route add -net 192.168.1.0/24 gw 192.168.2.2')
    ap2.cmd('route add -net 192.168.0.0/24 gw 192.168.2.1')
    '''
    sta1.cmd('route add -net 192.168.1.0/24 gw 192.168.0.100')
    sta1.cmd('route add -net 192.168.2.0/24 gw 192.168.0.100')
    sta2.cmd('route add -net 192.168.1.0/24 gw 192.168.0.100')
    sta2.cmd('route add -net 192.168.2.0/24 gw 192.168.0.100')
    '''

    makeTerm (ap2, cmd = "bash -c 'python3 veh_rsu_j.py;'")
    time.sleep(1)
    makeTerm (ap1, cmd = "bash -c 'python3 veh_rsu_i.py ;'")

    veh_rsui_auth_check = {} # for initial auth
    veh_rsuj_hand_auth_check = {}  # for handover to RSU j
    
    veh_rsu_assoc = {}  # for RSU handover

    ip_ct = 0
    while True :
        for sta in net.stations:
            if str(sta) not in veh_rsui_auth_check and sta.wintfs[0].associatedTo is not None : 
                veh_rsui_auth_check[str(sta)] = 0
                
                apx = sta.wintfs[0].associatedTo.node
                apx = str(apx)
                veh_rsu_assoc[str(sta)] = apx
                
                print ("---- Associated to AP1")
                if apx == 'ap1' and veh_rsui_auth_check[str(sta)] == 0:
                    # send NVID, HPW, p(x), h(x)
                    if str(sta) == 'sta1':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 test_veh_auth.py > auth_sta1.txt ;'") 
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py '20727c8d83557e47236fab04c3277974f462983a84ba245082706027c17d97d2' '42e0b8007bb6277143b1bad28bf187ef5c9b0eb68b4cf74e0fdd7f317c51df0e' '-793,5345,9864,-50,-5815,-2085,2297,-385' '-13,97,83,6,-55' > auth_sta1.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    if str(sta) == 'sta2':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py '49229d8f0b49c6294fceb79be540bd411452e1acdf88a369b1007e3e167bda69' 'a1cdcbecc76bef750e3ec22a86dd061e9112191c8c55947c45bae40989cd1e85' '-4899,-6011,-6822,-7368,716,-2941,1450' '71,83,21,50' > auth_sta2.txt;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1
                    
                    if str(sta) == 'sta3':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py '01b1bbe4659d87cef20b0b2ca6e913c2f2f24b5c651f0b4aa7522c098d2c10e5' '9713a32c7dfd794744f4ee65098395d661dcdda3650cf551d88bfa16a745f32a' '-5985,-4563,6965,4971,638,-1222' '-63,9,34,26' > auth_sta3.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    if str(sta) == 'sta4':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py '167ccc3d2ec5ff07d867c03e7e97e2902a7265f105e931b7654d86c7c34a6a75' '5ad694c31486d7cd80a704985e8ca6c9cc39458cc0bb1bef0bf885abb47bd976' '5856,-12192,-192,6528' '61,-66,-68' > auth_sta4.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    if str(sta) == 'sta5':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py '206124e7754b806786e62ff1b9a6c853b754f2f683229869df51ba7786293f5b' '60d7a849c1ff725eda494e307a5c563d5ec08dae2840f96c6ae9c4b7572b7cb0' '4752,7944,-3508,-3626' '-72,-80,98' > auth_sta5.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1
                    
                    if str(sta) == 'sta6':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py '2aba7a87934506f819813254c136a1bbc14797e4bf1f78ef210e58ba722b6b7f' '62fa7b399fab013cf0aebae2a6b67523288c63f00a59a421fcfe03662f7613f5' '-2079,504,4095,2937,7662,5603,4220,2911' '-63,63,84,96,71' > auth_sta6.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    if str(sta) == 'sta7':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py '2f4acd53d47a5ec5eee4a31292f628e03ee7f0ce67c163a12f5cbabeacea45ac' '7f09d1f600384beb8f098556f1a4000b77cde16ca4005a8636b5851c57a1c7d7' '-6708,-4132,9870,-740,-4186,1612' '86,-22,-39,26' > auth_sta7.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    if str(sta) == 'sta8':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py '3796dfac318ab67d7c3d0bf72f6e294fba2fd09eb4786c0945fa0e868b42cbc2' 'e45b34737643f221eda3973c24b52d03db77fec15f609d4dbb61fba30261221d' '8134,3783,2829,-1995,-1100' '-98,17,20' > auth_sta8.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    if str(sta) == 'sta9':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py '44278f83b22b9d720ca151cf7af0a6e8d13fb3f6500dbcab513dd9007e051327' 'a80244170f63ea027eae144dd8e6b2993b0fd0b0e5922562ae5d322f494a385d' '240,-608,-7256,-8340,7681,9718,2337' '-6,29,100,41' > auth_sta9.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    if str(sta) == 'sta10':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py '466e40ac4a451881632670276c0ca57766c696ef6f5ba4ecd2c80af42a568c5e' '9912be29f0825ef273850cb62fbd90656e1cd6785351a12d27f79fbfd59322e6' '-7802,-4196,-4809,2158' '94,80,83' > auth_sta10.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1
                    
                    if str(sta) == 'sta11':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py '4babdadad627c8825621ead9c4e772241134605cea683fba185fe8a0ed8e20b6' '216bd4fc8d058f24d66453fc2a126bde27835bef5fa3a410d67af7f8df141765' '777,1272,-5704,1843,222' '21,69,-37' > auth_sta11.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    if str(sta) == 'sta12':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py '4e8abb90f052c90260738d2c54e7d16bae78d49fca873e4058333fdca2011f84' '5ebb8e4266882debfd7ca78a18981fc30c77d1b2261e17027fe044920d5bef0f' '3230,8156,4729,-2766,-1755' '-95,6,27' > auth_sta12.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1
                    
                    if str(sta) == 'sta13':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py '6fe92c3a17e0e61f9e8cee2df8f46fce82d3b897a568d846420f2e0750434c2a' 'f31c1170f723f408b3467bcdf74c978be79d09dc43c18a57d030f8658adc83b4' '-1860,-6888,-11400,-6048' '-20,-56,-72' > auth_sta13.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    if str(sta) == 'sta14':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py '71aff6bfe9159666d9b4e278cfd4bf4831ae8caa0eedc7492c26dcbd71640250' '10630dec7a017c9bf3434e34487af2b35a0cb3c78c1e5aa5f95cb276c4b1af9e' '-154,-947,-1410,2007,6804' '11,48,81' > auth_sta14.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    if str(sta) == 'sta15':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py '72872804554c30fc537490dea4654b214476ce3a0e87c9b1c2e43690eeb4ef1f' 'cf9260064284d22364823bc5de1f9cbf6b45d941c62209d1795c25b6d1dc63a9' '-450,3315,2715,-1919,-1485,6910,-7160,4514' '45,51,-36,-64,74' > auth_sta15.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1
                    
                    if str(sta) == 'sta16':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py '7551a4d0b161e4224e3fc2e7bbd9f5803078e44cdd263d2eba71f81d895abc3f' 'ce21ffe477b55e52b47d79e9b9064b8c6d0c783fef73560fc93bd22994aeeb90' '2430,5001,625,5680' '81,-25,80' > auth_sta16.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    if str(sta) == 'sta17':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py '7a7b3b22791b20b969d4d1c8f5097878371dcf17966122c1dee74d079c8fd2f4' 'f5de37a76cad5f4159c15c1ec316eb99a76eabe0940331e0e9a0538e75a71429' '1410,-784,349,-199,-36' '47,-23,-4' > auth_sta17.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    if str(sta) == 'sta18':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py '7b248d0abeddff3a4963f4cf1ab60b899f2f6909d32b43dbacfa945eb3d3073f' '7b248d0abeddff3a4963f4cf1ab60b899f2f6909d32b43dbacfa945eb3d3073f' '-4424,-10060,-8977,-3289,-113,66' '79,95,43,-6' > auth_sta18.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1
                
                    if str(sta) == 'sta19':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py '7cf844bd0c67f5b6f7e8867991b27deb0dd3348b44bf4bb3ff12d65af5eb600a' 'fa300fc38b75a71d2460dc2ebdfb961334565901be0c529ee46b55550efeba21' '-2528,-2286,-2362,-2053,-8459,1897,-594,-1325' '-32,-50,-30,27,-25' > auth_sta19.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    if str(sta) == 'sta20':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py '8e4de1caab4913cb6f44d53ecf2f56279c5511330ebb99bf357e10861366aca2' 'a6166a538c1392407655cdffca2d5dae55ee78f4bfc0b1ef1bc06ccdc032400a' '-780,-4495,-6680,-4365,-1575,-395,-70' '-12,-59,-51,-14' > auth_sta20.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1
                    
                    if str(sta) == 'sta21':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py 'a565d5e00ad654db7348c81b448125b3eed51c3c40f2b80e95dcaf35ccc6aee3' 'da58ac9dd48759052936ed642553c7a260d7201d6d42ab86f50ac3e7da775c49' '2256,1284,-3970,5260,6190,-770,718,-2604' '94,77,-13,-4,-31' > auth_sta21.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    if str(sta) == 'sta22':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py 'aceb4b9658cea768f7c23f55efb65d23f7593476758f86c1558b107e4d31e45e' 'f09fa16bb37dddd9223ef45c9e1c5bb9f7529f9b345b17a9b92f9fedc9399dbe' '378,-2408,6958,-4380,-7764,10584,1440,-3456' '-7,35,-84,-6,36' > auth_sta22.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    if str(sta) == 'sta23':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py 'bf0d5786876cc637a61ed6bb57efb5c0287386774acbe1a9bc90710f64bbb812' 'ff8a98d6a60292f2be25628629f25076c90c026b0ede69b94f3b03cbf6f1fd85' '224,-762,1320,-1134' '-14,24,-42' > auth_sta23.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    if str(sta) == 'sta24':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py 'ca773b30882e7f98d85f035a63a29b04945cb0ad7107673859804636d76c0c3d' '3cbccad2d7563d936566fd47af55297f666058b0517d8c9c92b680b73947dde6' '1892,-2976,7403,-4170,3076,724,-4740,-1872' '-44,16,-73,-94,-26' > auth_sta24.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    if str(sta) == 'sta25':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py 'd0f7239562d3a3921529f454e5c0034feacbf3a2b409eae1a134b515dff812fa' '4ed60d7ba86c06d30df1f33a9af909ed2ec091f609446c9aaadd257e923229b3' '893,-3542,-1469,6870,3870' '-47,38,86' > auth_sta25.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1
                    
                    if str(sta) == 'sta26':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py 'd54167773fe8c69a12608c1f5e875758e1f403b6c2c0b8fd44b7fa8318b886b2' '0e0e92cf9f2fb81c066c2ae87d8c4b44d0921175b0a533420165c3637ea0b6a2' '-975,-2075,-7715,-9385,-4595,-1148,-8922,186' '-65,-95,-35,-3,-93' > auth_sta26.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    if str(sta) == 'sta27':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py 'd665acee27d242b44f31b4a822e2dfcfe05de456d62760a0e97df0005ecd38c6' 'd496a33fe155021a5af62b9225832af232170daaf2eb6ffba654e8465a3abe91' '-1363,-5473,-7963,-5568' '47,85,87' > auth_sta27.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    if str(sta) == 'sta28':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py 'de71d98d008756c84179d114df9b552d97a26f563216273ec4917040bce219c8' '1f04103bf7b4398fc1a2be07e0bf873e10c44f7e99537dc50b65588b206266ff' '-4186,3510,7257,-7023,-596,4815,-770' '91,-13,-58,77' > auth_sta28.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    if str(sta) == 'sta29':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py 'fb15be31339cebb09bac0f3e0fe4b541666d6b77cf2d607bac061d358df864c8' 'fa8736409a3a834aace3b22bc2aa10c272f13052a084968af7e58ef11984dab2' '847,-5786,-5824,6022,463,-510' '-11,87,-23,-15' > auth_sta29.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    if str(sta) == 'sta30':
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_auth.py 'fec161480204b58092ddd3f9b845edb02d675731617bfd0430f89d62bd882d0a' '2a7a2af9492ac576bfea6e7163e21065d8e5dd330a31520b01b62b5919d37fea' '5451,-1800,3759,-1482,630,732' '69,-42,6,12' > auth_sta30.txt ;'") 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1
                    
                             
            elif str(sta) in veh_rsui_auth_check and sta.wintfs[0].associatedTo is not None : 
                apx = sta.wintfs[0].associatedTo.node
                apx = str(apx)
                veh_rsu_assoc[str(sta)] = apx   

                if apx == 'ap2' and str(sta) not in veh_rsuj_hand_auth_check:    
                    ip_ct = ip_ct + 1
                    IP = '192.168.1.' + str(ip_ct)
                    
                    print ("Handover ",str(sta)," associated with AP ", str(sta.wintfs[0].associatedTo.node))

                    if str(sta) == 'sta1':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta1-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py '86MPFA0' '7531' 'P10RKMU' '03H' > hand_sta1.txt ;'") # session key, r, VID, Hand_req
                        # x = makeTerm (sta, cmd = "bash -c 'python3 test_veh_hand.py > hand_sta1.txt ;'") # > hand_sta1.txt
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    if str(sta) == 'sta2':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta2-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py 'BMNKVWQ' '9966' 'M6QZPFE' '03H' > hand_sta2.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1
                    
                    if str(sta) == 'sta3':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta3-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py 'IEHJ26E' '9369' '4L828QX' '03H' > hand_sta3.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    if str(sta) == 'sta4':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta4-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py 'FMZU2PT' '6376' 'PKS1SMB' '03H' > hand_sta4.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    if str(sta) == 'sta5':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta5-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py '5RAI7WR' '7293' 'LG0CPOF' '03H' > hand_sta5.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    
                    if str(sta) == 'sta6':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta6-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py '41BWFLZ' '2814' '516DXJM' '03H'> hand_sta6.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1
                    
                    if str(sta) == 'sta7':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta7-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py 'KP5YVUP' '4925' 'JK542T5' '03H' > hand_sta7.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    if str(sta) == 'sta8':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta8-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py 'NHVNRRK' '4697' 'DOBIZTJ' '03H' > hand_sta8.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    if str(sta) == 'sta9':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta9-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py 'LAFYYPJ' '5811' 'ZO022MV' '03H' > hand_sta9.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    if str(sta) == 'sta10':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta10-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py 'TW212H8' '3507' 'GUGERYT' '03H' > hand_sta10.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1
                    
                    if str(sta) == 'sta11':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta11-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py 'VPO8C99' '2376' 'P267SQA' '03H' > hand_sta11.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    if str(sta) == 'sta12':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta12-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py 'N7T4R6G' '6800' '57HXGPN' '03H' > hand_sta12.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    if str(sta) == 'sta13':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta13-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py 'HMFYZHS' '8821' 'KBJ559J' '03H' > hand_sta13.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1
                    
                    if str(sta) == 'sta14':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta14-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py '4YO292N' '9117' '1PFBHG7' '03H' > hand_sta14.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    if str(sta) == 'sta15':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta15-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py 'AOOARRM' '2742' '9U0JHP9' '03H' > hand_sta15.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1
                    
                    if str(sta) == 'sta16':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta16-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py 'W9VL10C' '9407' '1D74PFF' '03H' > hand_sta16.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    if str(sta) == 'sta17':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta17-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py 'W01TD8V' '2226' 'O6F6J0O' '03H' > hand_sta17.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    if str(sta) == 'sta18':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta18-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py '3EJV4DL' '5836' 'QKSZKPY' '03H' > hand_sta18.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    if str(sta) == 'sta19':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta19-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py 'XOMDNWA' '7063' 'BURJ6CY' '03H' > hand_sta19.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    if str(sta) == 'sta20':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta20-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py 'X1LTLQF' '3906' 'ZHP3MN1' '03H' > hand_sta20.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1
                    
                    if str(sta) == 'sta21':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta21-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py 'MJEYPB8' '6653' '8RLKJ8W' '03H' > hand_sta21.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    if str(sta) == 'sta22':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta22-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py 'Y38BD3D' '6697' 'ITS3U0L' '03H' > hand_sta22.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    if str(sta) == 'sta23':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta23-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py '51FUUU7' '7180' '7JD5CF6' '03H' > hand_sta23.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    if str(sta) == 'sta24':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta24-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py '7AXJ417' '7176' 'TLHQBAL' '03H' > hand_sta24.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    if str(sta) == 'sta25':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta25-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py '7V1U923' '4665' '7ZEH8FU' '03H' > hand_sta25.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1
                    
                    if str(sta) == 'sta26':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta26-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py 'UHFY3OK' '4006' 'ZNAYK27' '03H' > hand_sta26.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    if str(sta) == 'sta27':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta27-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py 'GI2IHB7' '5212' '0528VXT' '03H' > hand_sta27.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    if str(sta) == 'sta28':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta28-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py 'XB2R48P' '6026' '2NL89XU' '03H' > hand_sta28.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    if str(sta) == 'sta29':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta29-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py 'CISYAYH' '3382' 'ED4V4EI' '03H' > hand_sta29.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    if str(sta) == 'sta30':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta30-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 veh_hand.py 'ZY0XGH1' '9079' 'Y2JM65I' '03H' > hand_sta30.txt ;'") # session key, r, VID, Hand_req
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1
                    
                    

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology(sys.argv)
