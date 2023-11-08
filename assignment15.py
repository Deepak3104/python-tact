age = int(input("Enter your age: "))
child_age_range = (0, 12)
teenager_age_range = (13, 19)
adult_age_range = (20, 64)
if age >= child_age_range[0] and age <= child_age_range[1]:
    category = "Child"
elif age >= teenager_age_range[0] and age <= teenager_age_range[1]:
    category = "Teenager"
elif age >= adult_age_range[0] and age <= adult_age_range[1]:
    category = "Adult"
else:
    category = "Senior"
print(f"You are categorized as a {category}.")