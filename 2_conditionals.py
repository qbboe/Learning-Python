import random       # modules
import sys
import os

print (" # CONDITIONALS:\n")

num = 3
fibo_list = [[1,1,2],[3,5,8] ]	#fibo_list.reverse()
random_num = random.randrange(1,6)

if num % 2 == 0 and num != 0 :
	print('even')
elif num % 2 -1 == 0 :
	print('odd')
else :
	print('not integer')

for num in range(0,10) :
	print(num**2,' ', end="")
print('online')	
for y in fibo_list :
	print(y)
for x  in range(0,2) :
	for y  in range(0,3) :
		print(fibo_list[x][y])

while(random_num % 2 != 0):
	print(random_num)
	random_num = random.randrange(1,6)

i = 0
while( i <= 20) :
	if ( i % 2 == 0 ) :
		print(i)
	elif( i == 9 ) :
		break 		# out of the loop
	else :
		i += 1
		continue	# back to while
	i += 1





print('\n' * 2)
