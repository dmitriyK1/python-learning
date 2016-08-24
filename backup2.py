import os
import time

print('Hi\n')
x = input('Propishite put` k papke, kotoruyu vam nuzhno bekapnut`:\n>>>')
y = input('Propishite put` k papke, kuda vy hotite sohranit` bekap\nPress Enter to save in /backups\n>>>')

if len(y) == 0:
	y = '/backups'

if not os.path.exists(y):
	os.mkdir(y)
	print('the folder', y, 'has being created')

comment = input('please, enter your comment:\n>>')

	
source = [x]
target_dir = y
today = target_dir + os.sep + time.strftime('%Y_%m_%d')
now = time.strftime('%H_%M_%S')

if not len(comment) == 0:
	now = now + '_'

if not os.path.exists(today):
	os.mkdir(today)
	print('the folder ', today ,' has being created')


target = today + os.sep + now + comment.replace(' ', '_') + '.zip'

zip_command = "zip {0} -qr {1}".format(target,' '.join(source))
print(zip_command)
if os.system(zip_command) == 0:
	print('backuped', target)
else:
	print('backup failed')
