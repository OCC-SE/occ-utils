import requests
import json
import sys
from contextlib import closing

# Get authorization token for future use
def login( url, app_key ):
	"Submit application key to login endpoint and receive authorization token"
	
	# Authorization parameter for grant type. Should be set to client_credentials
	payload = 'grant_type=client_credentials' 
	payload = payload.encode('utf-8') # data should be bytes

	# OAuth token should be set in Authorization header using value: Bearer <auth_token>
	headers = { 'Authorization' : 'Bearer ' + app_key , 'Content-Type' : 'application/x-www-form-urlencoded'}

	r = requests.post(url, data=payload, headers=headers)
	""" Set access token from JSON response. 
	Sample response:
	{
	token_type: "bearer"
	access_token: "[token]"
	}	
	"""
	return r.json()['access_token'];

	
# Get authorization token for future use
def login_admin( url, admin_name_pwd ):
	"Submit application key to login endpoint and receive authorization token"

	result = ""
	
	# Authorization parameter for grant type. Should be set to client_credentials
	payload = 'grant_type=password&' + admin_name_pwd
	payload = payload.encode('utf-8') # data should be bytes

	# OAuth token should be set in Authorization header using value: Bearer <auth_token>
	headers = { 'Content-Type' : 'application/x-www-form-urlencoded'}

	#print (url)
	try:
		r = requests.post(url, data=payload, headers=headers)
		""" Set access token from JSON response. 
		Sample response:
		{
		token_type: "bearer"
		access_token: "[token]"
		}	
		"""
		return r.json()['access_token'];
	except KeyError as err:
		print("URL: {0}; Key Error: {1}".format(url, err))
	except:
		print("Unexpected error:", sys.exc_info()[0])

	
# Perform logout operation
def logout( url, token ):
	"Perform logout operation"

	# OAuth token should be set in Authorization header using value: Bearer <auth_token>
	headers = { 'content-type': 'application/json', 'Authorization' : 'Bearer ' + token}
	
	r = requests.post(url, headers=headers)
	""" 
	Sample response:
	result 	boolean 	true - logout was success full, false - it failed.
	{
	  "result": true
	}
	"""
	if (r.status_code == requests.codes.ok):
		return r.json()['result'];


# Get JSON response from URL endpoint
def get( url, token, params ):
	"Get JSON response from URL endpoint"
	
	if token:
		#Auth token should be set in Authorization header using value: Bearer <auth_token>
		headers = { 'Authorization' : 'Bearer ' + token}
	
	r = requests.get(url, params=params, headers=headers)
	if (r.status_code == 200):
		return r.json();	   

# Get JSON response from URL endpoint
def get_store( url, params ):
	"Get JSON response from URL endpoint"
		
	r = requests.get(url, params=params, auth=('admin', 'admin'))
	if (r.status_code == 200):
		return r.json();
	
# Put data at URL endpoint
def put( url, token, payload, key ):
	"Put data at URL endpoint"
	
	# Auth token should be set in Authorization header using value: Bearer <auth_token>
	header = { 'content-type': 'application/json', 'Authorization' : 'Bearer ' + token}

	r = requests.put(url, data=json.dumps(payload), headers=header)
	if key:
		return r.json()[key]
	else: 
		return r.json();

# Put data at URL endpoint
def put_locale( url, token, payload, locale, key ):
	"Put data at URL endpoint"
	
	# Auth token should be set in Authorization header using value: Bearer <auth_token>
	header = { 'content-type': 'application/json', 'X-CCAsset-Language' : locale, 'Authorization' : 'Bearer ' + token}

	r = requests.put(url, data=json.dumps(payload), headers=header)
	#print (r.text)
	if key:
		return r.json()[key]
	else: 
		return r.json();
		
# Post data to URL endpoint
def post( url, token, payload ):
	"Post data to URL endpoint"
	
	# Auth token should be set in Authorization header using value: Bearer <auth_token>
	header = { 'Content-Type': 'application/json', 'Authorization' : 'Bearer ' + token}

	r = requests.post(url, data=json.dumps(payload), headers=header)
	#print (r.text)
	return r.json();	

# Post data to URL endpoint
def post_file( url, token, payload ):
	"Post data to URL endpoint"
	
	# Auth token should be set in Authorization header using value: Bearer <auth_token>
	header = { 'Content-Type': 'application/json', 'Authorization' : 'Bearer ' + token}

	r = requests.post(url, data=json.dumps(payload), headers=header)
	#print (r.text)
	return str(r.json()['token']);	

# Get JSON response from URL endpoint
def get_response_headers(url, header):
	"Get OCCS endpoint header info"

	'''
	By default, when you make a request, the body of the response is downloaded immediately. 
	You can override this behaviour and defer downloading the response body until you access the Response.content attribute with the stream parameter:
	'''
	with closing(requests.get(url, stream=True)) as r:
		return r.headers[header];	   	

# Download data from URL endpoint
def download_file( url, token, path ):
	"Download data from URL endpoint"

	# Auth token should be set in Authorization header using value: Bearer <auth_token>
	header = { 'Authorization' : 'Bearer ' + token}
	
	r = requests.get(url, headers=header, stream=True)
	if r.status_code == 200:
		with open(path, 'wb') as f:
			for chunk in r.iter_content(1024):
				f.write(chunk)
				
# Delete 
def delete( url, token ):
	"Delete URL endpoint"
	
	# Auth token should be set in Authorization header using value: Bearer <auth_token>
	header = { 'Content-Type': 'application/json', 'Authorization' : 'Bearer ' + token}

	r = requests.delete(url, headers=header)
	#print (r.text)
	return r.text;	
