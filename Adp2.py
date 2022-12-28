'''
import os,ipaddress #ipaddress is package
os.system('cls') #os.system will clear the console at the start of the execution
while True:
    ip=input('Enter IP address: ')
    try:
        print(ipaddress.ip_address(ip))
        print('IP valid')
    except:
        print('-'*50)
        print('IP is not valid')
    finally:
        if ip=='mango':
            print('script finished')
            break
            '''
#<package : ip address>.<ip_adress>.<attribute : ip>
''''
import os
print(os.system("ipconfig"))
'''
import socket
s=socket.socket()
print("socket is successfully created")
port=40674
s.bind(('',port))
print("socket binded to %s"% (port))
s.listen(5)
print("socket is listening")
while True:
    c,addr=s.accept()#single line multi variable assignment,to know value of c
    #print(c) or use debugger--pyDB is used for debugging
    print('Got connection from',addr)
    c.send(b,"Thank you for connecting")
    c.close()