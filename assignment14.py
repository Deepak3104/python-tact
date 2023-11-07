num = int(input("Enter a number: "))
if num < 1 or num > 10:
    print("Please enter a number between 1 and 10.")
else:
    print(f"Multiplication table for {num}:")
    for i in range(1, 11):
        product = num * i
        print(f"{num} x {i} = {product}")