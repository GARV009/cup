# Factorial using a loop with early return
def factorial_iterative_early_return(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
print(factorial_iterative_early_return(5))  # Output should be 120
