'''Write a python program to read contents of one file.Count total number of characters, lines, words and frequency 
of occurance of a particular word in the file'''

#Code:

file1=open("file1.txt","r")
char=0                         #it is a counter to count no of characters
Word_Count=0
occurance=0                    #counter to count occurances
wordlist=[]

word=input("Enter word which you want to be searched: ")

for line in file1:
	# open file in read mode to count number of characters
	for c in line:
		if c.isalpha():
			char=char+1

	wordlist=line.split(" ") 			#divides the string by spaces and save it in a list

	Word_Count=Word_Count + len(wordlist)

	# To search given word
	word_list=line.split(" ")                  #wordlist is a list of words

	for k in word_list:
		if k==word:
			occurance=occurance+1

print("Number of Characters are : ",char)
print("Number of Words are : ",Word_Count)
print("Word ",word,"found ",occurance,"times")

f2=open("file2.txt","a")

f2.write("Number of Characters are : ")
f2.write(char)

f2.write("Number of Words are : ")
f2.write(Word_Count)

f2.write("Occurance is")
f2.write(occurance)

f2.close()


#Output:
'''
nter word which you want to be searched: of
Number of Characters are :  104
Number of Words are :  19
Word  of found  2 times
'''
