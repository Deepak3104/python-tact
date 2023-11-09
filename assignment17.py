from faker import Faker
fake = Faker()
for i in range(1,51):
    print(f"{i}. {fake.address()}")
