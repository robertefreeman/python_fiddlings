# Simple site status script
# Author: @robertefreeman

import requests
import sys
import time


# Function to add http:// on addresses if not included in call
def url_normalizer(url):
	if str(url[0]+url[1]+url[2]+url[3]).lower() != 'http':
		addy = 'https://' + url
		return addy
	else:
		return url

# Function to log status data back to a .txt file
def logger(data):
	f = open("site_stat_log.txt", "a")
	f.write(data)
	f.close()

	# Open and read the file after the appending:
	# f = open("demofile2.txt", "r")
	# print(f.read())

# Function to push email notification if sites is not available	
def notifier():
	pass

# Function to delay site check 'secs' number of seconds
def timer(secs):
	print('\n\nChecking status ... \n')
	time.sleep(secs)

# Function to retrieve status code for a website
def check_site(url):
	for addy in url[1:]:
		
		try:
			r = requests.get(url_normalizer(addy))
			logger(str(addy + ': ' + r.status_code))
			print(f'The current status code for {addy} is:  {r.status_code}')
		except:
			logger(str(addy + ': Down'))
			print(f'The current status code of {addy} is: Down')

# program run 
for n in range(0,2):
	check_site(sys.argv)
	timer(1)
