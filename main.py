print("Hello World")

print("Hello Git")

def is_adult(age):
    return age >= 18

# Виклик функції, який поверне True або False
can_vote = is_adult(20) 
print(can_vote)  # Виведе: True

menu = ["wraps", "sandwiches", "soup", "salad"]
print("Our menu:")
for item in menu:
    print(item)

user_profile = {"name": "Wendy", "status": "active"}
print("\nUser data:")
for key in user_profile:
    print(f"{key}: {user_profile[key]}")

def greet():
    return "Hello"

print(greet(), "Wendy")  # Hello Wendy