from math import *

def fib(n):
	a = sqrt(5) 
	b = 1 / a * (pow((1 + a)/2, n) - pow((1 - a)/2, n))
	return b

n = int(input('Vvedite chislo ( menshe 100 ) : '))	
for i in range(0, n):	
	print(' ')
	print(int(fib(i)))
	# print(fib(i))
	
s = input('''
press to exit ''')		
		
