import random       # modules
import sys
import os

def addNumber(sNum,lNum) :# last and second last number
	sumNum = sNum + lNum
	return sumNum

print("How much numbers in Fibonacci's sequence do yuo want?")	
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
print(fibo_list )		# Fibonacci's sequence printed

x_list=[]	# interpolation nodes
y_fibo=[]	# fibonacci'values for nodes 
y_list=[]	# polynomial values
poles = 5	# number of nodes desired
delta = 0
matrix = []
def cumpute_delta (a,n) :
	delta = 0
	for i in range (0,poles) :   	# compute delta
		y_list.append(a*int(x_list[i])**n)
		r = int(a*x_list[i]**n)
		delta +=  (int(y_list[i] )- y_fibo[i])**2
		print(a,n ,poles,i,r,delta,'=(',y_list[i],'-', y_fibo[i],')^2')
	return delta
	
for i in range(0,poles) :
	x_list.append(list_lenght/(2*poles)+i*list_lenght/poles)
	y_fibo.append(fibo_list[int(x_list[i])])
print('x_list',x_list)		# interpolation nodes
print('y_fibo',y_fibo)		# fibonacci'values for nodes 

for a in range (0,3) :
	for n in range (0,2) :
		matrix = [ a,n,cumpute_delta (a,n)]
		print('matrix',matrix)
	
#print('y_list',y_list,'\n delta',delta)
#print('\nmatrix\n',matrix)


'''
import matplotlib.pyplot as plt

plt.plot([1,2,3,4])
plt.ylabel("Fibonacci's sequence")
plt.show()
'''