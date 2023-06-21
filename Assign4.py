'''To accept student's five courses marks and compute his/her result.Student is passing if he/she scores marks 
equal to and above 40 in each course. If student scores aggregate greater than 75%, then the grade is distinction. 
If aggregate is 60>=and <75, then the grade is first division. If aggregate is 50>= and <60, then the grade is 
second divison.If aggregate is 40>= and <50, then the grade is third division.'''

#Code 

p=int(input("Enter Physics marks :"))
g=int(input("Enter Graphics marks :"))
pps=int(input("Enter PPS marks :"))
b=int(input("Enter BEE marks :"))
m=int(input("Enter Maths marks :"))
agg=((p+g+pps+b+m)/5)
print("Aggregate Marks:",agg)

if (p>40) and (g>40) and (pps >40) and (b>40) and (m>40):
					if (agg>75) :
						print("Pass with distinction")
					elif (agg>=60) and (agg <75):
						print("Pass with First divison")
					elif (agg>=50) and (agg <60):
						print ("Pass with Second Division")
					elif (agg>=40) and (agg<50):
						print("Pass with Third Division")
else: 
	print("Fail")
	
#Output

'''
Enter Physics marks :95
Enter Graphics marks :96
Enter PPS marks :97
Enter BEE marks :97
Enter Maths marks :98
Aggregate Marks: 96.6
Pass with distinction


Enter Physics marks :70
Enter Graphics marks :70
Enter PPS marks :70
Enter BEE marks :70
Enter Maths marks :70
Aggregate Marks: 70.0
Pass with First divison


Enter Physics marks :38
Enter Graphics marks :39
Enter PPS marks :52
Enter BEE marks :57
Enter Maths marks :60
Aggregate Marks: 49.2
Fail
'''

