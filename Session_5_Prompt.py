'''
	Kevin Gustavo Roldan
	ASTR-19
	2025/10/14
'''

'''
Write a Python program that writes out a table of the function sin(x) vs. x, where x is tabulated between 0 and 2 with a
thousand entries. Follow the basic Python program structure, including a main program function.
'''

#--------------------------------------------------------{[ Imports ]}--------------------------------------------------------#

import numpy as np 					# Import Numpy
from astropy.table import Table 	# import the Table class
from astropy.io import ascii		# ascii plain text io
from astropy.io import fits			# FITS format io

#--------------------------------------------------------{[ Main ]}--------------------------------------------------------#

def main():

	x = np.linspace(0.,2.*np.pi,1000)			# A data array with a thousand entries from 0.0 to 2pi
	sinx = np.sin(x)								# Another array that calculates sin(x) for every entry in the x array

	data = Table([x, sinx], names = ['x','sin(x)'])			# Create a table
	ascii.write(data, 'table.txt', format = 'commented_header')	# Write the table to a new .txt file

	data_in = ascii.read('table.txt')									# read the data in
	print(data_in)

#----------------------------------------------------{[ Excecution Order ]}----------------------------------------------------#

if __name__=="__main__":
	main()