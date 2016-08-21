#! /usr/bin/env python3

from __future__ import print_function

if hasattr(__builtins__, 'raw_input'):
    input=raw_input

name = input('Please, enter your name: \n>>>')

shoplist = [' ']
shoplist2 = [' ']

print('\n====  Hi,', name, '!!!  ====')
print('''h - help
=====================================
''')
def menu():
	global a
	a = input('Do you want to create a new list? "y" -yes "q" -quit \n>>>')
	if a == ('y'):
		naz()
	else:
		print('GOODBYE!!!!')
		quit()
def menu2():
	global a
	a = input('Do you want to create a new list? "y" -yes "q" -quit \n>>>')
	if a == ('y'):
		naz2()
	else:
		print('GOODBYE!!!!')
		quit()
def naz():
	global b
	b = input('---------------------------\nPlease, enter the name of your list: \n>>>')
	if b == ('q'):
		print('GOOBYE!!!')
		quit()
	else:
		print('\n ======================================\n Enter your items ( to display press "enter" when completed print "end"): \n======================================')
		dod()
def naz2():
	global b
	b = input('---------------------------\nPlease, enter the name of your list: \n>>>')
	if b == ('q'):
		print('GOOBYE!!!')
		quit()
	else:
		print('\n ======================================\n Enter your items ( to display press "enter" when completed print "end"): \n======================================')
		dod2()
def dod():
	for item in shoplist:
		wr = "======My List contains {1} items:======\n{0}".format('\n'.join(shoplist), len(shoplist)-1)
		x = input('>>>')
		shoplist.append(x)
		f = open(name + (' ') + b, 'w')
		f.writelines(wr)
		f.write('\n========================================')
		f.close()
		
		if x == (''):
			del shoplist[0]
			print(wr)
		if x == ('end'):
			menu2()
		if x == ('h'):
			print(
'''You are abble to form your to-buy list
----Press ENTER after writing your item
---After completing entering all list, press ENTER one more time to display your list
---Your list will be saved in the file *your_name.txt
q - quit
''')
		else:
			dod()
def dod2():
	for item in shoplist2:
		wr2 = "======My List contains {1} items:======\n{0}".format('\n'.join(shoplist2), len(shoplist2)-1)
		x = input('>>>')
		shoplist2.append(x)
		f = open(name + (' ') + b, 'w')
		f.writelines(wr2)
		f.write('\n========================================')
		f.close()
		if x == (''):
			del shoplist2[0]
			print(wr2)
		if x == ('end'):
			print('Goodbye!')
			quit()
		if x == ('h'):
			print(
'''You are abble to form your to-buy list
----Press ENTER after writing your item
---After completing entering all list, press ENTER one more time to display your list
---Your list will be saved in the file *your_name.txt
q - quit
''')
		else:
			dod2()
menu()


