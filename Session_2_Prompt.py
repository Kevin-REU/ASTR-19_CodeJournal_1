'''
	Kevin Gustavo Roldan
	ASTR-19
	2025/10/02
'''

#============={[Starting Variables]}=============#

# Initial floats
a = 3.0
b = 9.0
#Intitail integers
c = 3
d = 9


# I have yet to make this work lmao
'''
#============={[Starting Variables]}=============#

# Calculates the sum of two floating point numbers
def Sumab():
	a + b
# Calculates the difference between two integers
def Difference():
	abs(c - d)
# Calculates the product of floating point number and an integer
def Product():
	a * c
'''

############################################################################################################################################

# This defines our main() function for this program
def main():
	print("\n\n")																		# Print Spacer

	# Introduction to the program
	print("We will be calculating the sum, difference, and products of floating point numbers and integers.\n\n")

	print(a," + ",b," = ",a + b,"which is a",type(a+b),"\n")										# Prints the data type, and answer of the sum
	print("The Differce between",c,"and",d,"is",abs(c - d),"which is a",type(abs(c - d)),"\n")	# Prints the data type, and answer of the difference
	print(a," * ",c," = ",a * c,"which is a",type(a * c),"\n")									# Prints the data type, and answer of the product

	print("\n\n")																					# Print Spacer

############################################################################################################################################

# When we run this program this executes first
if __name__=="__main__":
	main()