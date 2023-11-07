c=input("Enter any single alphabet character:")
if len(c)==1 and c.isalpha():
    c=c.lower()
    if c in ['a','e','i', 'o', 'u']:
        print("Given character is a Vowel")
    else:
        print("Given character is not a Vowel")
else:
    print("Please enter the valid single alphabet character")
