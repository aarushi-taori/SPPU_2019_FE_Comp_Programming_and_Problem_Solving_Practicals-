'''Create class STORE to keep track of Produts (Product code, Name and Price). Dislay menu of all products to user. Generate bill as per order'''


#Code: 
class store:
	__prod_code=[]
	__prod_name=[]
	__cost_price=[]
	__prod_quan=[]

	def getdata(self):
		self.p=int(input("Enter no. of products you need to store: "))
		for x in range(self.p):
			self.__prod_code.append(input("Enter Product Code: "))
			self.__prod_name.append(input("Enter Product Name: "))
			self.__cost_price.append(int(input("Enter Product price: ")))

	def display(self):
		print("Stock in Stores")
		print("Product Code \t\t Product Name \t\t  Cost Price")
		for x in range(self.p):
			print(self.__prod_code[x],"\t\t",self.__prod_name[x],"\t\t",self.__cost_price[x])

	def print_bill(self):
		total_price = 0
		for x in range(self.p):
			q=int(input("Enter the quantity for the product code %s: "%self.__prod_code[x]))
			self.__prod_quan.append(q)
			total_price = total_price+self.__cost_price[x]*self.__prod_quan[x]
		print(" \t\t Invoice Receipt \t\t")
		print("Product Code \t Product Name \t  Cost Price \t Quantity \t Total Amount")
		for x in range(self.p):
			print(self.__prod_code[x], "\t\t", self.__prod_name[x], "\t\t",self.__cost_price[x], "\t\t", self.__prod_quan[x], "\t\t",self.__prod_quan[x]*self.__cost_price[x])
		print("Total Amount = ",total_price)

S=store()
S.getdata()
S.display()
S.print_bill()

#OUTPUT:
'''
Enter no. of products you need to store: 2
Enter Product Code: STAT001
Enter Product Name: Ink Pen 
Enter Product price: 25
Enter Product Code: GROSS003
Enter Product Name: Rice
Enter Product price: 50
Stock in Stores
Product Code 	     Product Name      Cost Price
STAT001 		 Ink Pen  	    25
GROSS003 		 Rice 		    50
Enter the quantity for the product code STAT001: 2
Enter the quantity for the product code GROSS003: 3
 		 Invoice Receipt 		
Product Code 	 Product Name 	  Cost Price 	    Quantity 	    Total Amount
STAT001          Ink Pen  	       25 		 2 		 50
GROSS003         Rice 		       50 		 3 		 150
Total Amount =  200
'''

'''
            
            
       
