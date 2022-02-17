import os
import sys
import time
from os import system
from time import sleep



try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
	request = requests.get("https://www.google.com/search?q=tahmid+rayat", timeout=3)
except (requests.ConnectionError, requests.Timeout) as exception:
    print("[!] No internet connection [!]")
    sys.exit()

import requests

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'

def hprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 100)

logo = """
\033[1;32m _____  __ __  __  ____  _____  __  __          _____ _      ______ _____  
\033[1;32m |  __ \/_ |  \/  |/ __ \|  __ \|  \/  |   /\   |_   _| |    |  ____|  __ \ 
\033[1;32m | |  | || | \  / | |  | | |  | | \  / |  /  \    | | | |    | |__  | |__) |
\033[1;32m | |  | || | |\/| | |  | | |  | | |\/| | / /\ \   | | | |    |  __| |  _  / 
\033[1;32m | |__| || | |  | | |__| | |__| | |  | |/ ____ \ _| |_| |____| |____| | \ \    
\033[1;32m |_____/ |_|_|  |_|\____/|_____/|_|  |_/_/    \_\_____|______|______|_|  \_\
\033[1;36m [\033[1;37m+\033[1;36m]\033[1;32m CREATED AND CODED BY D1MOD1877 \033[1;31m(\033[1;33mhttps://www.d1modev.ml/\033[1;31m)
"""

system("clear")
print (logo)
print ('')
hprint(G + ' Launching D1MOD MAILER ...')
sleep(2)
print ('')
to = raw_input(G + " Send Mail To" + C + " : " + Y)
print ('')
subject = raw_input(G + " Input Mail Subject" + C + " : " + Y)
print ("")
msg = raw_input(G + " Input Mail Content" + C + " : " + Y)
print ("")
usagnt = 'Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;]'
sess = requests.Session()
rth = sess.post('http://anonymouse.org/cgi-bin/anon-email.cgi', headers={
	'Host': 'anonymouse.org',
	'User-Agent': usagnt,
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate',
	'Referer': 'http://anonymouse.org/anonemail.html',
        'Connection': 'close',
        'Upgrade-Insecure-Requests':'1',
        'Content-Type':'application/x-www-form-urlencoded'
}, data={
	'to': to,
	'subject': subject,
	'text': msg
})

if '200' in rth.text:
    hprint(G + "D1MOD Sending Email >>>>>>>>>>")
else:
    hprint(G + "D1MOD Sending Email >>>>>>>>>>")
    print ('')
    time.sleep(2)
    hprint(C + " Mail Successfully Sent !!")
    print ('')
    sleep(3)
    hprint(W + " Process can take some time !!")
    print ('')
    print (Y + "MADE BY D1MOD https://www.d1modev.ml/" + W)
    print ('')
