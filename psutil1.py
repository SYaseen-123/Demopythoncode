## 1 packet=255 bytes
#mountpoint is a entry point of the path
#fstype='NTFS'
# file system type:
# a.FAT32 b.NTFS---mostly used
#opts -storage options--fixed
'''

import psutil#psutil can do low level network interactions
#result01 = psutil.cpu_times()
#result02=psutil.cpu_stats()
#result03=psutil.cpu_freq()
#result04=psutil.disk_partitions()

result05=psutil.net_io_counters(pernic=True)
#pernic=false:True: :collect the snetio info from all the NIC's together display the overall result

#print(result01)
#print(result02)
#print(result03)
#print(result04)
print(result05)
'''

import psutil
network_stats=psutil.net_io_counters(pernic=False)
bytes_sent=getattr(network_stats,'bytes sent')
bytes_recv=getattr(network_stats,'bytes recv')
print("Bytes Sent ={0} |Bytes Received ={1} ".format(bytes_sent,bytes_recv))


