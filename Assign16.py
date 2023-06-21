'''Write a python program to copy the contents of one file to another. While copying contents do the following:
1.)Replace all commas with fullstop.
2) Replace all uppercase letters with lower case letters 
3) Replace all lowercase letters with uppercase letters'''

#Code :

file1=open("file1.txt","r")
file2=open("file2.txt", "w")

for line in file1: 
	#read the file line by line 
	#read a sentence 

	#replace "," with "."
	line=line.replace(", ", ".")

	#swapcase
	line=line.swapcase()

	print(line)
	file2.write(line)


#Output :
'''bHUBANESHAR IS AN IMPORTANT cITY OF oDISHA.

oDISHA IS FAMOUS FOR rATHAYATRA FESTIVAL OF lORD jAGANNATH.bALADEV AND sUBHADRA.
'''



