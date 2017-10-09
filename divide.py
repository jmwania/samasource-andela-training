def divide(a,b):
	try:
		if b > 0:
			return a/b
	except ZeroDivisionError:
		return "not divisible by Zero"
	except TypeError:
		return " :-) only number"
print divide(9,0)
print divide(9,3)
print divide(9,'a')
