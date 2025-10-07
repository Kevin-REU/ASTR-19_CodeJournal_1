'''
	Kevin Gustavo Roldan
	ASTR-19
	2025/10/07
'''

import numpy as np				# Import Numpy Library

# Define a function "f" that returns a value
def f(x):
	return x**3 + 8				# Calculates and returns x^3 + 8

# Define the main function
def main():

	# Initialize y with a chosen value
	y = 9

	# Call function "f" with a value of x = 9, and print the result
	print(f(y))					

	# If the value of f(9) is greater than 27, print "YAY!"
	if(f(y) > 27):
		print("YAY!")	
	# If the value of f(9) is less than or equal to 27, print "Damn Bruh :("		
	if(f(y) <= 27):
		print("Damn Bruh :(")	

# Commands the program to execute "main" first
if __name__ == '__main__':
	main()