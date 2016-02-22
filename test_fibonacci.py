def test_fibonacci():
    """
    In this function we import the module fibonacci.py,
    and test it the function Fibonacci against known
    values.
    Fibonacci(n)
    """
    import fibonacci as fb
    assert fb.Fibonacci(10) == 55
    assert fb.Fibonacci(5) == 5
	