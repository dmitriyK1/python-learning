import os
import time

print('Hi\n')
x = input('Propishite put` k papke, kotoruyu vam nuzhno bekapnut`:\n>>>')
y = input('Propishitr put` k papke, kuda vyhotite sohranit` bekap:\n>>>')

source = [x]
target_dir = y

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip {0} -qr {1}".format(target,' '.join(source))
print(zip_command)
if os.system(zip_command) == 0:
	print('backuped', target)
else:
	print('backup failed')
