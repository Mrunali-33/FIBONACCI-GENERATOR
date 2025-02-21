def fibonacci_generator(n):
    """Generator function for Fibonacci series up to n terms"""
    a, b = 0, 1  # Initialize first two Fibonacci numbers
    count = 0
    while count < n:
        yield a  # Yield the current Fibonacci number
        a, b = b, a + b  # Update values for next iteration
        count += 1

# Get user input for number of terms
num_terms = int(input("Enter the number of Fibonacci terms: "))

# Generate and print the Fibonacci series
print("Fibonacci Series:")
print(list(fibonacci_generator(num_terms)))
