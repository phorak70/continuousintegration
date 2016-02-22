import unittest

class FibExceptions(unittest.TestCase):
	def test_fibonacci(self):
		import fibonacci as fb
		assert fb.Fibonacci(10) == 55
		assert fb.Fibonacci(5) == 5
	
	def test_Fibonacci_throws_exception(self):
		import fibonacci as fb
		self.assertRaises(ValueError, fb.Fibonacci, -5)
	
	def test_Fibonacci_float_handling(self):
		import fibonacci as fb
		self.assertRaises(ValueError, fb.Fibonacci, 5.1)
	