a, b = 0, 1
n = 10
fibonacci_sequence = []
for j in range(n):
    fibonacci_sequence.append(a)
    a, b = b, a + b
for i, number in enumerate(fibonacci_sequence, start=1):
    print(f"{i}. {number}")