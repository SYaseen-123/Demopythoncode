import os
with open("ip_list.txt") as file:
    park=file.read()
    #reding the values,tripping of double quotes also by read function
    park=park.splitlines()
    print("{park} \n")
for ip in park:
    response=os.popen(f"ping {ip} ").read()
    if("request time out." or "unreachable") in response:
        print(response)
        f=open("info_output.txt","a")
        f.write(str(ip)+'list is up'+'\n')
        f.close()
    else:
        print(response)
        f=open("info_output1.txt","a")
        f.write(str(ip)+'list is down'+'\n')
        f.close()
with open("info_output1.txt") as file:
    output=file.read()
    print(output)
    f.close()
with open("info_output.txt","w") as file:
    pass
#pass is a place holder or (skip when the code is notavailable ads of now)

import os,ipaddress
os.system('cls')
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

