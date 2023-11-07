def greatestOfThree(A,B,C):
    if A>B and A>C:
        l=A
    if B>A and B>C:
        l=B
    if C>A and C>B:
        l=C
    print("The greatest of three number is",l)
A=int(input("Enter the first number:"))
B=int(input("Enter the second number:"))
C=int(input("Enter the third number:"))
greatestOfThree(A,B,C)