'''\nExtension Upload Example Script
Usage: python upload_extension.py -e <env> -u <user> -p <password> -n <name> -f <folder>
Arguments:
 -e, --env			environment (required)
 -u, --user			user(required)
 -p, --password		password(required)
 -n, --name			name(required)
 -f, --folder		extension folder (required)

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
import remove_extension

def usage():
	print (__doc__)
	sys.exit(2)

def import_file(host, token, file, extension_name):		
	
	#Upload file 
	print ('Start file upload. File: ', file)

	#Set URLS
	files_url = occ_properties.files_url.format(root_url=host)

	#Assume each file requires only 1 segment to upload
	payload = {'segments': '1', 'filename': extension_name}

	file_token = occ_requests.put_locale(files_url, token, payload, 'en', 'token')
	print ('File Token = ' + str(file_token))
	
	#Upload file
	with open(file, 'rb') as f:
		encoded = base64.b64encode(f.read())

	#ASCII encoding needed	
	encoded = encoded.decode('ascii')
		
	payload = {'index': '0', 'token': file_token, 'filename': extension_name, 'file': encoded}
	start_file_upload_url = files_url + '/' + file_token
	print ('Post file to: ' + start_file_upload_url)
	s = occ_requests.post(start_file_upload_url, token, payload)
	#print ('result = ' + json.dumps(s))
	
def zip_extension(name, target_dir):            
    
	deploy_path = os.path.dirname(target_dir) + "/deploy"
	print("deploy_path: " + deploy_path)

	if not os.path.exists(deploy_path):
		os.mkdir(deploy_path);
	zip_file = deploy_path + "/" + name.replace(" ", "_") + '.zip'

	if os.path.exists(zip_file):
		os.remove(zip_file)

	zip = zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED)
	rootlen = len(target_dir) + 1
	for base, dirs, files in os.walk(target_dir):
		for file in files:
			fn = os.path.join(base, file)
			zip.write(fn, fn[rootlen:])
	return zip_file
			
def update_extension_metadata(extension_id, name, folder):		
	
	default_data = {}
	default_data["createdBy"]="Oracle"
	default_data["name"]= name
	default_data["version"]=1
	default_data["timeCreated"]="2019-01-01"
	default_data["description"]="Sample extension"

	data = {}

	#Open metadata file (ext.json) in extension folder
	try:
		with open(folder + '/ext.json', 'r') as f:  
			data = json.load(f)
			print(data)
	except (IOError, ValueError):
		print('Error: using default metadata')
		data = default_data

	#Update new extension id
	data['extensionID'] = extension_id
	data['name'] = name

	#Write updated metadata
	with open(folder + '/ext.json', 'w') as f:  
		json.dump(data, f)

def find_applicationId(host,token,name):
	#Get list of extensions
	extension_url = occ_properties.applications_ids_url.format(root_url=host)
	result = occ_requests.get(extension_url, token, None)

	repositoryId=""
	#Find extension by name and return repositoryId
	#print(result)
	if result:
		for item in result["items"]:   
			if (item["name"] == name):
				print ("Found extension: " + item["name"])
				repositoryId = item["repositoryId"]
				break

	if not repositoryId:
		print(name + " Extension not Found")
	

	return repositoryId

def upload_extension(env, user, pwd, name, folder):		
	print ('START Upload Extension Example')

	#Login with password credentials
	host = occ_properties.host.format(env=env)
	login_url = occ_properties.oauth_login_mfa_url.format(root_url=host)
	pwd_credentials = occ_properties.mfa_app_key.format(user=user,pwd=pwd)
	print ('Get login auth from: ' + login_url)
	token = occ_requests.login_admin(login_url, pwd_credentials)
	
	if token:
		print ('Login success!')


		extension_id = find_applicationId(host,token,name)
		print("extendsion_id: " + extension_id)

		if not extension_id:
			#Create new extension id
			applications_ids_url = occ_properties.applications_ids_url.format(root_url=host)
			payload = {"name":name,"type":"extension"}
			result = occ_requests.post(applications_ids_url, token, payload)

			#Retrieve extension id from result
			extension_id = result["id"]
			print(extension_id)
		
		#Update metadata file (ext.json) in extension folder with new extensionID
		update_extension_metadata(extension_id, name, folder)
					
		#Zip extension archive
		zip_file = zip_extension(name, folder)

		#Upload extension archive
		extension_name = '/extensions/' + zip_file
		import_file(host, token, zip_file, extension_name)
		
		#Create & validate new extension
		extension_url = occ_properties.extensions_url.format(root_url=host)
		#print ("Post Extension URL: " +extension_url)
		payload = {"name":zip_file}
		result = occ_requests.post(extension_url, token, payload)
		print (result)

		success = result['success']

		if success:
			print("OCC Success: {}".format(success))
		else:
			print("OCC Success: False")

		#Logout
		logout_url = occ_properties.oauth_logout_url.format(root_url=host)
		if occ_requests.logout(logout_url, token) :
			print ('Logout success!')
		
		

	print ('END Upload Extension ' + name)

def main(argv):
	
	# Set default url & response header values
	env, user, pwd, name, folder = ('', 'admin', 'admin', 'Test Extension', '')	
		
	try:
		opts, args = getopt.getopt(argv,"he:u:p:n:f:",["env", "user", "password", "name", "folder"])
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
		elif opt in ("-f", "--folder"):
			folder = arg			
		elif opt in ("-n", "--name"):
			name = arg

	if not env or not folder:
		usage()

	print ('*** Name = ', name, '; Folder = ', folder, " ***")

	upload_extension(env, user, pwd, name, folder)
		
	print ("Done!")
	
if __name__ == "__main__":
   main(sys.argv[1:])		

