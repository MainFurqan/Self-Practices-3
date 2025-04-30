"""
✅ Task:
-> Create a Python dictionary with student info:

python
{
  "id": 101,
  "name": "Hamza",
  "course": "Python",
  "active": True
}

-> Convert it to a JSON string and print it.
-> Then save it to a file named student.json.
"""

import json

student_info = {
  "id": 101,
  "name": "Hamza",
  "course": "Python",
  "active": True
}

data = json.dumps(student_info, indent=4)
print(data)

with open("student.json", "w") as file:
    json.dump(student_info, file, indent=4)
