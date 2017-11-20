import random       # modules
import sys
import os

primes_list = []
count = 0
found = 0
notprime = 0
for num in range (2, 10000) :
	found = 0
	for i in primes_list : 
		if(num % i) == 0 :
			found = 1
			break
	if found == 0	 :
		primes_list.append(num)
		count +=1				
print(primes_list,count)		

# 4,25,168,1229,9592
# 2 5  13  35   98






