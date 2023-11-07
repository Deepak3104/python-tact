import math
def fact(n):
    return(math.factorial(n))
n = int(input("Enter the positive number:"))
f = fact(n)
print("Factorial of", n, "is", f)