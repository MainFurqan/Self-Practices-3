# Q2: Create a Dictionary
# Given two lists:
# keys = ["name", "age", "course"]
# values = ["Furqan", 21, "Python"]
# Task: Use zip() to create a dictionary from these two lists.

keys = ["name", "age", "course"]
values = ["Furqan", 21, "Python"]

output = dict(zip(keys, values))

print(output)