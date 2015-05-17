# !/user/bin/python
# Filename: bak_03.py

import os
import time



source=['/home/guibiaob/python_code/by1','/home/guibiaob/python_code/by2']

target_dir='/home/guibiaob/python_code/'


today=target_dir + time.strftime('%Y%m%d')

now=time.strftime('%H%M%s')

comment=raw_input('Enter a comment -->')

if len(comment)==0:
	target=today + os.sep +now + '.zip'
else:
	target=today + os.sep +now + '_' +\
		comment.replace(' ','_')+'.zip'



if  not os.path.exists(today):
	os.mkdir(today)
	print 'successfully created directory ',today

zip_command="zip -qr '%s' %s" % (target,' '.join(source))

if os.system(zip_command)==0:
	print 'Successful backup to',target

else:
	print 'backup falied'





