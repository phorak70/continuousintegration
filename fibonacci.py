def Fibonacci(n):
	"""
	Return the n-th value of the Fibonacci sequence
	[0, 1, 1, 2, 3, 5, 8, 13, ...]
	"""
	if n < 0:
		raise ValueError("n must be greater than zero")
	elif round(n) != n:
		raise ValueError("n must be a whole number")
	elif n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return Fibonacci(n-1) + Fibonacci(n-2)
	