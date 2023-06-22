'''
Create class EMPLOYEE for storing details (Name, Designation, gender, Date of Joining and Salary). Define function members to compute
a) total number of employees in an organization
b) count of male and female employee
c) Employee with salary more than 10,000
d) Employee with designation "Asst Manager
'''

#Code :

class employee:                    #class variable
	empcount=0
	malecount=0
	femalecount=0
	emp10k=0
	asstman=0
	s=10000
	def newemp():              #class method
		a=input("Enter Employee Name : ")
		b=input("Enter Designation of Employee : ")
		c=input("Enter gendar of an employee (M/F) : ")
		d=int(input("Enter salary of employee : "))
		e=int(input("Enter date of joining in DDMMYYYY : "))
		print("Imformation of employees stored Successfully !!!")
		employee.empcount+=1
		if c=="M":
			employee.malecount+=1
		if c=="F":
			employee.femalecount+=1
		if b=="asst.manager":
			employee.asstmant+=1
		if d>=10000:
			employee.emp10k+=1

ch=0
while True :
	print("1.Add new employee in software")
	print("2.Display employee count")
	print("3.Display male count")
	print("4.Display asst.manager count")
	print("5.Display employee with salary more than 10000 count")
	print("Press any key to exit")
	ch=int(input("Enter your choice : "))
	if ch==1 :
		employee.newemp()
	elif ch==2 :
		print("Total employeee are : ",employee.empcount)
	elif ch==3 :
		print("Total male employees are : ",employee.malecount)
		print("Total female employees are : ",employee.femalecount)
	elif ch==4 :
		print("Total assistant manager  are : ",employee.asstman)
	elif ch==5 :
		print("Employees having salary more than 10000 are :",employee.emp10k)
	else :
		print("Exiting the program")
		break



#OUTPUT :

'''
1.Add new employee in software
2.Display employee count
3.Display male count
4.Display asst.manager count
5.Display employee with salary more than 10000 count
Press any key to exit
Enter your choice : 1
Enter Employee Name : Aarushi
Enter Designation of Employee : Manager
Enter gendar of an employee (M/F) : F
Enter salary of employee : 80000
Enter date of joining in DDMMYYYY : 01092018
Imformation of employees stored Successfully !!!
1.Add new employee in software
2.Display employee count
3.Display male count
4.Display asst.manager count
5.Display employee with salary more than 10000 count
Press any key to exit
Enter your choice : 9
Exiting the program
'''
