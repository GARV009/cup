# Factorial using tail recursion
def factorial_tail_recursive(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return factorial_tail_recursive(n - 1, n * accumulator)

# Example usage
print(factorial_tail_recursive(5))  # Output should be 120
