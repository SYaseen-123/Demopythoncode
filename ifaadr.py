'''
import ifaddr
adapters=ifaddr.get_adapters()
for adapter in adapters:
    print("Ips of network adapters "+adapter.nice_name)#nice_name method fetches 0r collects the name of the adpter
    for ip in adapter.ips:
        print("%s/%s"%(ip.ip,ip.network_prefix))
        '''

# if u wish to include network interfaces that do not have a configured IP address,pass the include_unconfigured param
#Adapters with no configured IP addresses will have an zero-length ips property
#802.11ac :IEEE standard code::wireless LAN

import ifaddr
adapters=ifaddr.get_adapters(include_unconfigured=True)
for adapter in adapters:
    print("Ips of network adapters " + adapter.nice_name)  # nice_name method fetches 0r collects the name of the adpter
    if adapter.ips:
        for ip in adapter.ips:
            print("%s/%s" % (ip.ip, ip.network_prefix))
    else:
        print("No IPs configured")
