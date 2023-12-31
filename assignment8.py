def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
print("Prime numbers between 1 and 100:")
for num in range(1, 101):
    if is_prime(num):
        print(num, end=' ')