import math

def ppcm(a, b):
    """Returns the least common multiple (LCM) of two numbers."""
    if a == 0 or b == 0:
        return 0  # LCM of 0 and any number is 0
    return abs(a * b) // math.gcd(a, b)  # Using GCD to calculate LCM
