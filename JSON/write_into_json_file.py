import json

data = {
    "name" : "Furqan",
    "age" : 20,
    "skills" : ["Python", "ML", "Data Science"]
}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4) 