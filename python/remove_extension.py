'''\nExtension Remove Example Script
Usage: python remove_extension.py -e <env> -u <user> -p <password> -n <name>
Arguments:
 -e, --env			environment (required)
 -u, --user			user(required)
 -p, --password		password(required)
 -n, --name			name(required)

Flags:
 -h      help
'''     
import sys
import getopt
import json
import base64
import os
import zipfile
import occ_requests
import occ_properties

def usage():
	print (__doc__)
	sys.exit(2)

	
def find_extension(host,token,name):
	#Get list of extensions
	extension_url = occ_properties.extensions_url.format(root_url=host)
	result = occ_requests.get(extension_url, token, None)

	repositoryId=""
	#Find extension by name and return repositoryId
	#print(result)
	for item in result["items"]:   
		if (item["name"] == name):
			print ("Found extension: " + item["name"])
			repositoryId = item["repositoryId"]
			break

	if not repositoryId:
		print(name + " Extension not Found")
	

	return repositoryId


	

def remove_extension(env, user, pwd, name):		
	print ('START Remove Extension Example')

	#Login with password credentials
	host = occ_properties.host.format(env=env)
	login_url = occ_properties.oauth_login_mfa_url.format(root_url=host)
	pwd_credentials = occ_properties.mfa_app_key.format(user=user,pwd=pwd)
	print ('Get login auth from: ' + login_url)
	token = occ_requests.login_admin(login_url, pwd_credentials)
	
	if token:
		print ('Login success!')

		#Get list of extensions
		#extension_url = occ_properties.extensions_url.format(root_url=host)
		#result = occ_requests.get(extension_url, token, None)

		repositoryId=find_extension(host,token,name)
		#Find extension by name and return repositoryId
		#for item in result["items"]:   
		#	if (item["name"] == name):
		#		print ("Found extension: " + item["name"])
		#		repositoryId = item["repositoryId"]
		#		break
		
		if repositoryId:
			#Get list of extensions
			extensions_id_url = occ_properties.extensions_id_url.format(root_url=host,id=repositoryId)
			print ("Deactivate Extension URL: " +extensions_id_url)
			payload = {"op":"deactivate"}
			result = occ_requests.post(extensions_id_url, token, payload)
			print (result)
			
			#Check if successful
			#print (result["success"])
			if (result["success"] == True):
				#Delete extension
				print ("Delete Extension URL: " +extensions_id_url)
				result = occ_requests.delete(extensions_id_url, token)
				
				if result:
					print("OCC Success: False")
					print(result)
				else:
					print("OCC Success: True")
			else:
				print ("Extension deactivate not sucessful: " + name)
				print("OCC Success: False")

		
		#Logout
		logout_url = occ_properties.oauth_logout_url.format(root_url=host)
		if occ_requests.logout(logout_url, token) :
			print ('Logout success!')

	print ('END Remove Extension Example')

def main(argv):
	
	# Set default url & response header values
	env, user, pwd, name = ('', 'admin', 'admin', 'Test Extension')	
		
	try:
		opts, args = getopt.getopt(argv,"he:u:p:n:",["env", "user", "password", "name"])
	except getopt.GetoptError:
		usage()
   
	for opt, arg in opts:
		if opt == '-h':
			usage()
		elif opt in ("-e", "--env"):
			env = arg			
		elif opt in ("-u", "--user"):
			user = arg			
		elif opt in ("-p", "--password"):
			pwd = arg			
		elif opt in ("-n", "--name"):
			name = arg

	if not env or not user or not pwd:
		usage()

	print ('*** Name = ', name, " ***")

	remove_extension(env, user, pwd, name)
		
	print ("Done!")
	
if __name__ == "__main__":
   main(sys.argv[1:])		

