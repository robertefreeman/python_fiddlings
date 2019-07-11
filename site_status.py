import requests
import sys

def url_normalizer(url):
	for addy in url:
		# if str(addy[0]+addy[1]+addy[2]+addy[3]).lower != 'http':
		#	addy = 'https://' + addy
		pass

def timer():
    pass
    
def check_site(url):
	for addy in url:
		url_normalizer(addy)
		r = requests.get(addy)
		print(f'The current status code for {addy} is:  {r.status_code}')
		

check_site(sys.argv)

	

	

