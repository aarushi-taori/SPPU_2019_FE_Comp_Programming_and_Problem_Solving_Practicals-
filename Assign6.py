'''To simulate simple calculator that performs basic tasks such as addition, subtraction, multiplication and 
division with special operations like computing x^y and x!'''

#Code 

import math
ch=0
while ch!=7:
	print(" CALCULATOR " )
	print("Select which operation to perform")
	print("1. Press 1 for Addition")
	print("2. Press 2 for Subtraction")
	print("3. Press 3 for Multiplication")
	print("4. Press 4 for Division")
	print("5. Press 5 for Power Operation")
	print("6. Press 6 for Factorial Operation")
	print("7. Press 7 for Exit")
	ch=int(input("Enter your Choice : "))
	if (ch>=1) and (ch<=5):
			num1=int(input("Enter the First number : "))
			num2=int(input("Enter the Second number : "))
	if ch==1:
		sum1=num1+num2
		print("The Addition of the numbers is : ",sum1)
	elif ch==2:
		sub=num1-num2
		print("The Subtraction of the numbers is : ",sub)
	elif ch==3:
		multi=num1*num2
		print("The Multiplication of the numbers is : ",multi)
	elif ch==4:
		quo=num1/num2
		rem=num1%num2
		print("The Division of the numbers gives quotient : ",quo," and Remainder : ",rem)
	elif ch==5:
		pow1=math.pow(num1,num2)
		print("The power operation of ",num1," raised to ",num2,"gives : ",pow1)
	elif ch==6:
		num=int(input("Enter the number whose factorial is to be found : "))
		flag=1
		while num>0:
			flag=flag*num
			num=num-1
		print("The factorial of number is : ",flag)
	elif ch==7:
		print("Exiting the Calculator")
		break
	else:
		print("Wrong Input")
		
		
# OUTPUT 
'''
 CALCULATOR 
Select which operation to perform
1. Press 1 for Addition
2. Press 2 for Subtraction
3. Press 3 for Multiplication
4. Press 4 for Division
5. Press 5 for Power Operation
6. Press 6 for Factorial Operation
7. Press 7 for Exit
Enter your Choice : 1
Enter the First number : 10
Enter the Second number : 8
The Addition of the numbers is :  18
 CALCULATOR 
Select which operation to perform
1. Press 1 for Addition
2. Press 2 for Subtraction
3. Press 3 for Multiplication
4. Press 4 for Division
5. Press 5 for Power Operation
6. Press 6 for Factorial Operation
7. Press 7 for Exit
Enter your Choice : 2
Enter the First number : 10
Enter the Second number : 20
The Subtraction of the numbers is :  -10
 CALCULATOR 
Select which operation to perform
1. Press 1 for Addition
2. Press 2 for Subtraction
3. Press 3 for Multiplication
4. Press 4 for Division
5. Press 5 for Power Operation
6. Press 6 for Factorial Operation
7. Press 7 for Exit
Enter your Choice : 3
Enter the First number : 3
Enter the Second number : 4
The Multiplication of the numbers is :  12
 CALCULATOR 
Select which operation to perform
1. Press 1 for Addition
2. Press 2 for Subtraction
3. Press 3 for Multiplication
4. Press 4 for Division
5. Press 5 for Power Operation
6. Press 6 for Factorial Operation
7. Press 7 for Exit
Enter your Choice : 4
Enter the First number : 7
Enter the Second number : 3
The Division of the numbers gives quotient :  2.3333333333333335  and Remainder :  1
 CALCULATOR 
Select which operation to perform
1. Press 1 for Addition
2. Press 2 for Subtraction
3. Press 3 for Multiplication
4. Press 4 for Division
5. Press 5 for Power Operation
6. Press 6 for Factorial Operation
7. Press 7 for Exit
Enter your Choice : 5
Enter the First number : 2
Enter the Second number : 3
The power operation of  2  raised to  3 gives :  8.0
 CALCULATOR 
Select which operation to perform
1. Press 1 for Addition
2. Press 2 for Subtraction
3. Press 3 for Multiplication
4. Press 4 for Division
5. Press 5 for Power Operation
6. Press 6 for Factorial Operation
7. Press 7 for Exit
Enter your Choice : 6
Enter the number whose factorial is to be found : 6
The factorial of number is :  720
 CALCULATOR 
Select which operation to perform
1. Press 1 for Addition
2. Press 2 for Subtraction
3. Press 3 for Multiplication
4. Press 4 for Division
5. Press 5 for Power Operation
6. Press 6 for Factorial Operation
7. Press 7 for Exit
Enter your Choice : 9
Wrong Input
 CALCULATOR 
Select which operation to perform
1. Press 1 for Addition
2. Press 2 for Subtraction
3. Press 3 for Multiplication
4. Press 4 for Division
5. Press 5 for Power Operation
6. Press 6 for Factorial Operation
7. Press 7 for Exit
Enter your Choice : 7
Exiting the Calculator
'''

 
 
	
