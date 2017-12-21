'''
 A squared square is a square made of squares.
 All the squares have to be different sizes.
 The smallest one has dimensions 120. 
'''
import sys
import random

maxsteps = 10000 
dim  =  120
biggest = dim / 2	# guessed max square length 
area = 0 
list = []
steps = 0
end = 0
def sq (num):
	return num**2

while steps < maxsteps:						# avoid infinite loop
	steps = steps + 1						
	while (area < dim**2 + 1):				# don't overshoot the area
		if area == dim**2:					# right area
			list.sort()						
#			print('Eureka!',list)
			end = 1
			for i in range (1, len(list)):	# check same number twice 
				if (list[i] - list[i-1]) == 0:
					end = 0
			if end == 1:
				print('Eureka!',list, end)
				sys.exit(1-end)				
		x = random.randrange(1, biggest, 1)	# compute random number
		area = area + sq(x)					# square it
		list.append(x)							
	area = 0								# reset initial conditions
	list = []
#print(area,list)