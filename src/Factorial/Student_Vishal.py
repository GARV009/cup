# Slightly modified recursive factorial
def compute_factorial(n):
    return 1 if n == 0 else n * compute_factorial(n - 1)

# Example usage
print(compute_factorial(5))  # Output should be 120
