'''
from netmiko import ConnectHandler
CSR={
    "device_type": "cisco_ios",

    "ip":"sandbox-iosxe-latest-1.cisco.com",
   # "ip":"sandbox-iosxe-recomm-1.cisco.com",
    "port":22,#netkon--32,,SSH-port 223
    "username":"developer",
    "password":"C1sco12345"
}
net_connect=ConnectHandler(**CSR)
hostname=net_connect.send_command('show run | i host')
hostname.split(" ")
hostname,device,*rest=hostname.split(" ")
print("Backing up" + device)
filename="C:/Users/user715/PycharmProjects/pythonProject/device02.txt"
showrun=net_connect.send_command('show run')
showvlan=net_connect.send_command('show vlan')
showver=net_connect.send_command('show ver')
log_file=open(filename,"a")
log_file.write(showrun)
log_file.write("\n")
log_file.write(showvlan)
log_file.write("\n")
log_file.write(showver)
log_file.write("\n")
net_connect.disconnect()
'''

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#address from the internet
print(s)
