import requests
import sys

def url_normalizer(url):
    pass

def timer():
    pass
    
def check_site(url):
	for addy in url:
		url_normalizer(addy)
		r = requests.get(addy)
		print(f'The current status code for {addy} is:  {r.status_code}')
		

check_site(sys.argv)

	

	

