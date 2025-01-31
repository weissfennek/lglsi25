def fibonacci(n):
    """
    Calculates the nth Fibonacci number.

    Args:
        n: The index of the desired Fibonacci number (non-negative integer).

    Returns:
        The nth Fibonacci number.
        Raises ValueError if n is negative.
        Returns 0 if n is 0
        Returns 1 if n is 1 or 2
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b