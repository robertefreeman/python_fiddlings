import requests
import sys
import time

def url_normalizer(url):
	if str(url[0]+url[1]+url[2]+url[3]).lower() != 'http':
		addy = 'https://' + url
		return addy
	else:
		return url

def timer(secs):
	print('\n\nChecking status ... \n')
	time.sleep(secs)


def check_site(url):
	for addy in url[1:]:
		# print(url_normalizer(addy))
		r = requests.get(url_normalizer(addy))
		print(f'The current status code for {addy} is:  {r.status_code}')

for n in range(0,10):
	check_site(sys.argv)
	timer(5)
