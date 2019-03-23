# Import the necessary packages
from consolemenu import *
from consolemenu.items import *
import netifaces
from modules import *

# def getASCII():
#     r=""
#     r+="    _   ______ _       ________"
#     r+="\n"
#     r+="        / | / / __ \ |     / / ____/"
#     r += "\n"
#     r+="       /  |/ / / / / | /| / / __/   "
#     r += "\n"
#     r+="      / /|  / /_/ /| |/ |/ / /___   "
#     r += "\n"
#     r+="     /_/ |_/\____/ |__/|__/_____/   "
#     r += "\n"
#     r+="                                    "
#     return r


# import sys
# import time
# from consolemenu import *
#
# def spinning_cursor():
#     while True:
#         for cursor in ['|', '/','-', '\\']:
#             yield cursor
#
# spinner = spinning_cursor()
# for _ in range(50):
#     sys.stdout.write(next(spinner))
#     sys.stdout.flush()
#     time.sleep(0.1)
#     sys.stdout.write('\b')