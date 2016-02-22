class FibExceptions(unittest.TestCase):

    def test_fibonacci(self):
        """
        In this function we import the module fibonacci.py,
        and test it the function Fibonacci against known
        values.
        Fibonacci(n)
        """
        import fibonacci as fb
        assert fb.Fibonacci(10) == 55
        assert fb.Fibonacci(5) == 5

    def test_Fibonacci_throws_exception(self):
        """
        We test here that when a negative value is passed as n
        to the Fibonacci function, it throws an exception.
        """
        import fibonacci as fb
        self.assertRaises(ValueError, fb.Fibonacci, -5) 


    def test_Fibonacci_float_handling(self):
        """
        Tests that input is an integer
        """
        import fibonacci as fb
        self.assertRaises(ValueError, fb.Fibonacci, 5.1)