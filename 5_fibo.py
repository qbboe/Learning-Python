import random       # modules
import sys
import os

def addNumber(sNum,lNum) :# last and second last number
	sumNum = sNum + lNum
	return sumNum

print('How much numbers in Fibonacci sequence do yuo want?')	
list_lenght 	 = sys.stdin.readline()
list_lenght = int(list_lenght)
fibo_list = [0,1]
dim = len(fibo_list)
lNum = fibo_list[dim-1]
sNum = fibo_list[dim-2]

while (dim < list_lenght) :
	dim = len(fibo_list)
	lNum = fibo_list[dim-1]
	sNum = fibo_list[dim-2]
	fibo_list.append(addNumber(sNum,lNum))
print(fibo_list )

'''
import matplotlib.pyplot as plt

plt.plot([1,2,3,4])
plt.ylabel("Fibonacci's sequence")
plt.show()
'''