'''import socket
s=socket.socket()
port=40674
s.connect(('127.0.0.1',port))
print(s.recv(1024))
s.close()
'''
from netmiko import ConnectHandler #netmiko is package ,connecthandler is module
#connectHandler--connects to a specific type of vendor devices
#Different types of protocols:SSH
#netmiko is used for network devices
#with netmiko we can connect and play with different devices,based on the vendors
CSR={
    "device_type": "cisco_ios",
    "ip":"sandbox-iosxe-latest-1.cisco.com",
     "port":204, "username":"developer",
    "password":"C1sco12345"
}
net_connect=ConnectHandler(**CSR) #**CSR denotes--connection paramters--what are the
#output_host=net_connect.send_commandi host')
#rint(output_runhost)
output=net_connect.send_command('show ip int brief')
print(output)
#utput_clock=net_connect.send_command('show clock') #int ,ip,brief,ip,ro are API-application programming interface
#rint(output_clock)
#utput_routes=net_connect.send_command('show ip ro')
#rint(output_routes)
#utput_runconfig=net_connect.send_command('show run')
#rint(output_runconfig)



net_connect.disconnect()
#if u didnt close the connection the connection remains open