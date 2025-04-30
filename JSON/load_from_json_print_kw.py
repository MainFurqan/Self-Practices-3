"""
Q: 1) Load the JSON data using Python
2) Print each key and value line by line
"""

import json

try:
    with open("data.json", "r") as file:
        content = json.load(file)
except FileNotFoundError:
    print("Error: data.json file not found.")

if isinstance(content, dict):
    for key, value in content.items():
        print(f"{key} : {value}")
else:
    print("The JSON data is not dictionary.")