input_string = input("Enter a string: ")
input_string = input_string.lower()
vowel_count = 0
vowels = "aeiou"
for char in input_string:
    if char in vowels:
        vowel_count += 1
print("Number of vowels in the string:", vowel_count)