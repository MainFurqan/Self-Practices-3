"""
🔹 Q4: KeyError in Dictionary
Task:
You have a dictionary:

python
user = {"name": "Ali", "age": 30}
Try to access user["email"].

Handle the error with a custom message: "Email key not found."
"""
# 🔹 Q4: Handle KeyError in Dictionary Access

user = {"name": "Ali", "age": 30}

try:
    key = input("Enter the key you want to access (e.g., name, age, email): ").strip()
    print(f"{key.capitalize()} : {user[key]}")
except KeyError:
    print(f"'{key}' key not found in the user data.")
