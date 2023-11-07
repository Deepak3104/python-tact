original_string = input("Enter a string: ")
reversed_string = ""
for i in range(len(original_string) - 1, -1, -1):
    reversed_string += original_string[i]
print("Reversed string:", reversed_string)