# Q1: Merge Two Lists
# Given:
# names = ["Ali", "Sara", "Furqan"]
# scores = [85, 90, 95]
# Task: Use zip() to combine them into a list of strings like:

# ["Ali scored 85", "Sara scored 90", "Furqan scored 95"]


names = ["Ali", "Sara", "Furqan"]
scores = [85, 90, 95]

output = []
for name, score in zip(names, scores):
    res = f"{name} scored {score}"
    output.append(res)

print(output)