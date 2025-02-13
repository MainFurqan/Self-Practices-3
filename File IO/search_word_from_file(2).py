# Ask to user enter input
search_word = input("Search here.........")

with open("practice.txt", "r") as f:
    data = f.read()
    # check the search word exist or not
    if (data.find(search_word) != -1):
        print(f"{search_word} is exist.")
    else:
        print(f"{search_word} is not exist.")