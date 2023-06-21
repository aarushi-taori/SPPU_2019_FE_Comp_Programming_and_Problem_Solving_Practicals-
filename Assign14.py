'''To accept from user the number of Fibonacci numbers to be generated and print the Fibonacci series '''

#CODE:

x=0
y=1
num=int(input("Enter the limit of the series : "))
print(x,y,end=' ')
for i in range(num):
	z=x+y
	x=y
	y=z
	print(x,end=' ')
	
	
#OUTPUT:
'''
Enter the limit of the series : 5
0 1 1 1 2 3 5

Enter the limit of the series : 13
0 1 1 1 2 3 5 8 13 21 34 55 89 144 233
'''

