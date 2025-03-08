# Factorial using functools.reduce
from functools import reduce

def factorial_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

# Example usage
print(factorial_reduce(5))  # Output should be 120
