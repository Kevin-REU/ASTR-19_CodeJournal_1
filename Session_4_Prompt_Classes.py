'''
	Kevin Gustavo Roldan
	ASTR-19
	2025/10/09
'''

# Define a class with an initialized set of parameters

#--------------------------------------------------------{[ Imports ]}--------------------------------------------------------#

# Import sys
import sys					

#--------------------------------------------------------{[ Classes ]}--------------------------------------------------------#

# A class for my favorite animal and it's characteristics
class Snake:
	
	def print(self):
		print("\n")
		print(" My favorite animal:...")
		print(f" Has arms of length: {self.len_arms}")
		print(f" Has this many eyes: {self.num_eyes}")
		print(f" Has a tail?:        {self.has_tail}")
		print(f" Is furry?:          {self.Is_furry}")
		print("\n")

	def __init__(self, larms = 0.0, neyes = 2, htail = True, furry = False):
		self.len_arms = larms
		self.num_eyes = neyes
		self.has_tail = htail 
		self.Is_furry = furry

#--------------------------------------------------------{[ Main ]}--------------------------------------------------------#

def main():

	# Set the Animal's Default Characteristics
	larms = 0.0
	neyes = 2
	htail = True
	furry = False

	# If there are at least 2 command line arguments, set neyes equal to the second
	if(len(sys.argv) >= 2):
		neyes = int(sys.argv[1])

	# If there are at least 3 command line arguments, set larms equal to the third
	if(len(sys.argv) >= 3):
		larms = float(sys.argv[2])

	# Initialize our Snake
	our_snake = Snake(larms = larms, neyes = neyes, htail = htail, furry = furry)

	# Print our information about our Snake
	our_snake.print()

#----------------------------------------------------{[ Excecution Order ]}----------------------------------------------------#

# Run our program 
if __name__ == "__main__":
	main()