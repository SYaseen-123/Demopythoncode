#code refractoring-----writig different logics to code or problem

from getmac import get_mac_address as gma
print(gma())

import uuid
print(hex(uuid.getnode()))

import uuid
print("The MAC address in formatted way is :",end=" ")
print(':'.join(['{:02x}'.format((uuid.getnode()>>ele)&0xff)# : is used for seperation,02x-hexadecimal,,,,0xff--it is range
for ele in range(0,8*6,8)][::-1]))#ele is a datacontainer-----8*6[8 bits and 6 parts]....-1 is negative indexing
#reverse indexing ---from bottom of line