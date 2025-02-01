def is_perfect(n):
    if n < 1:
        return False

    # Find divisors of n
    divisors = [i for i in range(1, n) if n % i == 0]
    
    # Check if the sum of divisors equals n
    return sum(divisors) == n

# Test the function
number = 6
if is_perfect(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
