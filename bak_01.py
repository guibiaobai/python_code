# !/user/bin/python
# Filename: bak_01.py

import os
import time

source=['/home/guibiaob/python_code/by1','/home/guibiaob/python_code/by2']

target_dir='/home/guibiaob/python_code/'


target=target_dir+time.strftime('%Y%m%d%H%M%S')+'.zip'

zip_command="zip -qr '%s' %s" % (target,' '.join(source))

#print zip_command

#exit()

if os.system(zip_command)==0:
	print "successful backup to",target
else:
	print 'Backup Failed'
