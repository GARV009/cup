# Factorial using recursion
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage
print(factorial_recursive(5))  # Output should be 120
