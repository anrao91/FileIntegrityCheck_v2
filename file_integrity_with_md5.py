import os
import subprocess

cmd = subprocess.call(["ssh", "user@server", "~/md5script"])

os.system('~/Code/md5script')

os.system('~/Code/file_integrity_check')

flag = False
result = os.popen('md5sum -c md5sum.txt').readlines() 
for status in result:
	file_name, status_type = i.split(':')
	
	if status_type.strip() != "OK" :
		flag = True
		print ("Status: [] - File [] has changed".format(status_type, file_name))

if not flag:
	print "Success"