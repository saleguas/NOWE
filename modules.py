import os, sys, netifaces, random, scapy.all

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