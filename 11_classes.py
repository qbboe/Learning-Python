'''
data and function -> attributes and methods
'''
class Employee:
	pass	# do nothing
	
emp_1 = Employee()  # instance of class
emp_2 = Employee()

emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'cs@email.com'
emp_1.pay = '50'

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'tu@email.com'
emp_2.pay = '40'
'''
too long, use init method
'''
class Employee:
	def __init__(self, first, last, pay):	# "self", attributes
		self.first = first	# instance variables
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@email.com'
	
emp_1 = Employee('Corey', 'Schafer', '50')  # self not needed
emp_2 = Employee('Test', 'User','40')

print (emp_1.first, emp_1.last)	
#  or
print ('{} {}'.format( emp_1.first,  emp_1.last))
'''
too stupid
'''
class Employee:
	def __init__(self, first, last, pay):	# "self", attributes
		self.first = first	# instance variables
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@email.com'
	def fullname(self):	# clever method
		#return '{} {}'.format( self.first,  self.last)
		return self.first+' '+self.last

emp_1 = Employee('Corey', 'Schafer', '50')  # self not needed
emp_2 = Employee('Test', 'User','40')

print (emp_2.fullname())	# ()needed it's a method, not an attribute 
# or
#print (Employee.fullname(emp_2))