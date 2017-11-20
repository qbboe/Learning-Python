'''mport random       # modules
import sys
import os
'''
def main():
	print("Guess a number")
randomnumber = 55
found = False
while not found :
	userGuess = input("Your Guess: ")
	if userGuess == randomnumber :
		print("You got it!")
		found = True
	elif (userGuess > randomnumber) :
		print("Guess lower!")
	else:	
		print("Guess higher!")
		

if __name__ == "__main__":	
		main()
		
	