words = ["apple", "banana", "cherry", "date"]

sea_word = input("Enter search word: ")

for index, value in enumerate(words):
    if(sea_word == value):
        print(f"Index of {value} is {index}")

