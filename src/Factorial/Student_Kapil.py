# Factorial using a loop
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
print(factorial_iterative(5))  # Output should be 120
