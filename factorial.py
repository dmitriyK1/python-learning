
def fact(n):
	if n == 0:
		return 1
	else: 
		return n * fact(n-1)	
		
print('0 - to exit')
while True:		
	print(' ')
	n = int(input('Factorial.. Vvedite chislo ( menshe 100 ) : '))	
	if n == 0:
		break
	else:	
		print(n,'! =',fact(n))