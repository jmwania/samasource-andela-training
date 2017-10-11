def divide(a,b):
	"""divide two numbers"""
	try:
		return a/b
	except ZeroDivisionError:
		return "(:- what did you do? you Can't divide by zero"
	except TypeError:
		return " :-) only number"