# !/user/bin/python
# Filename: bak_02.py

import os
import time


source=['/home/guibiaob/python_code/by1','/home/guibiaob/python_code/by2']

target_dir='/home/guibiaob/python_code/'


today=target_dir+time.strftime('%Y%m%d')

now=time.strftime('%H%M%S')


if not os.path.exists(today):
	os.mkdir(today)
	print 'successfully created directroy',today

target=today+os.sep+now+'.zip'

zip_command=" zip -qr '%s' %s" % (target,' '.join(source))


if os.system(zip_command)==0:
	print 'successful backup to',target
else:
	print 'backup falied'


