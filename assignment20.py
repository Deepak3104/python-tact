def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
if __name__ == "__main__":
    try:
        num_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))
        if num_terms <= 0:
            print("Please enter a positive integer.")
        else:
            fib_sequence = fibonacci_sequence(num_terms)
            print(f"Fibonacci sequence up to {num_terms} terms:")
            print(fib_sequence)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")