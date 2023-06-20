'''To calculate the salary of an employee given his basic pay (take input from user).Calculate salary of employee.Let HRA be10% of basic 
pay and TA be 5% of basic pay. Let employee pay professional tax as 2% of total salary. Calculate net salary payable after deductions.'''

#Code :

BS=int(input("Enter Basic Salary :"))
HRA=(BS*10)/100
TA=(BS*5)/100
GROSS=BS+HRA+TA
PT=(GROSS*2)/100
NET=GROSS-PT 
print ("Basic Salary of the Employee is: ",BS)
print ("HRA is: ",HRA)
print ("TA is: ",TA)
print ("Gross Salary of the Employee is: ",GROSS)
print ("Professional tax is: ",PT)
print ("Net Salary of the Employee is: ",NET)


#Output :
'''
Enter Basic Salary :80000
Basic Salary of the Employee is:  80000
HRA is:  8000.0
TA is:  4000.0
Gross Salary of the Employee is:  92000.0
Professional tax is:  1840.0
Net Salary of the Employee is:  90160.0
'''

