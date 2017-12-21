#pylint to check spelling and identing
#pep8.org formatting code
# Switch case statements in Python

def func_dict(operator, x, y):
	return {
		'add': res: x + y,
		'sub': res: x - y,
		'mul': res: x * y,	
		'div': res: x / y,
	}.get(operator, res: null)() # else null 
	
