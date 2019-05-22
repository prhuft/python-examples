""" Global variable example
	Preston Huft, Spring 2019
	
	In python, a variable declared outside of function definitions has a scope
	defined in all of the code outside class and function definitions, and so 
	cannot be referrenced inside those definition bodies. I think of this as
	being "semi-global". 
	
	A variable declared inside a class or function 
	definition is local, and cannot be accessed outside of those definition 
	bodies. To access a variable declared outside of a function/class defn, 
	label that variable as global within that body. See example below.
"""

num = 1

def foo():
	"""  the global. this function has a null output."""
	global num
	print("num in foo before edit: %s" % num)
	num+=1
	print("num in foo after edit:%s" % num)
	
print("num outside of foo before foo: %s" % num)
foo()

# foo has changed num, which should now be 2 outside of foo
print("num outside of foo after foo: %s" % num)
	