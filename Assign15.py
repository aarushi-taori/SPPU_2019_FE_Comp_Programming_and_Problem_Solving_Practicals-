'''Write a python program that accepts a string from the user and performs following string operations :
1. Calculate Length of the String
2. String Reversal
3. Equality Check of two Strings
4. Check Palindrome
5. Check Substring '''


print("""1.Enter 1 for Length of string
2.Enter 2 for Reverse of String 
3.Enter 3 to check equality of two strings
4.Enter 4 to check whether given input is a palindrome 
5.Enter 5 to check substring""") 
ch = int(input("Enter your choice : "))
if ch>=1 and ch<=5:
	if ch==1:
		str1 = input("Enter your string: ")
		a=len(str1)
		print("Length of given string is :", a)
	elif ch==2:
		str1 = input("Enter your string: ")
		r= str1[::-1]
		print("Reverse of given string is :", r)
	elif ch==3:
		str1 = input("Enter your string: ")
		str2 = input("Enter 2nd string to check equality:")
		if str2==str1:
			print("Both strings are equal")
		else:
			print("Both strings are not equal")
	elif ch==4:
		str1 = input("Enter your string:")
		str2 = str1[::-1]
		if str2==str1:
			print("Given string is a palindrome")
		else:
			print("Given string is not a palindrome")
	elif ch==5:
		str1 = input("Enter your string:")
		str2 = input("Enter required substring :")
		if str2 in str1:
			print(str2, " is a substring of ", str1)
		else:
			print(str2, " is not a substring of ", str1)
else:
	print("Wrong Choice !!")
	

#OUTPUT :
'''
.Enter 1 for Length of string
2.Enter 2 for Reverse of String 
3.Enter 3 to check equality of two strings
4.Enter 4 to check whether given input is a palindrome 
5.Enter 5 to check substring
Enter your choice : 1
Enter your string: Python
Length of given string is : 6


1.Enter 1 for Length of string
2.Enter 2 for Reverse of String 
3.Enter 3 to check equality of two strings
4.Enter 4 to check whether given input is a palindrome 
5.Enter 5 to check substring
Enter your choice : 2
Enter your string: Python
Reverse of given string is : nohtyP

1.Enter 1 for Length of string
2.Enter 2 for Reverse of String 
3.Enter 3 to check equality of two strings
4.Enter 4 to check whether given input is a palindrome 
5.Enter 5 to check substring
Enter your choice : 3
Enter your string: Python
Enter 2nd string to check equality: Python 
Both strings are equal


1.Enter 1 for Length of string
2.Enter 2 for Reverse of String 
3.Enter 3 to check equality of two strings
4.Enter 4 to check whether given input is a palindrome 
5.Enter 5 to check substring
Enter your choice : 4 
Enter your string:nitin
Given string is a palindrome

1.Enter 1 for Length of string
2.Enter 2 for Reverse of String 
3.Enter 3 to check equality of two strings
4.Enter 4 to check whether given input is a palindrome 
5.Enter 5 to check substring
Enter your choice : 5
Enter your string:Python 
Enter required substring :yth
yth  is a substring of  Python

'''


	  

