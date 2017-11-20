import random       # modules
import sys
import os

test_file = open("test.txt","wb")	# write
print(test_file.mode)		# wb: write mode
print(test_file.name)		
test_file.write(bytes("Write me to the file \n", 'UTF-8')) 	# WRITE
test_file.close()

test_file = open ("test.txt","r+")	# reading and writing
test_in_file = test_file.read()		#READ
print(test_in_file)

test_file.close()
os.remove("test.txt")
