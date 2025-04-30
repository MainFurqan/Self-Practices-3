"""
You have a file employees.json:

json
[
  {"name": "Ali", "salary": 50000},
  {"name": "Sara", "salary": 60000}
]
✅ Task:

-> Load the JSON data
-> Add a new employee: {"name": "Zara", "salary": 70000}
-> Save the updated list back to employees.json
"""
import json

with open("employees.json", "r") as file:
    data = json.load(file)


new_employee = {"name": "Zara", "salary": 70000}
data.append(new_employee)

print(data)

with open("employees.json", "w") as file:
    data = json.dump(data, file, indent=4)
