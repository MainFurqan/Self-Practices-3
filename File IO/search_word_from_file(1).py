import re

# Ask to user enter input
search_word = input("Search here.......").strip()

# Initialize found variable  
found = False

# open file in read mode
with open("practice.txt", "r") as fr:
    for word in fr.read().split():    # split content into words
        cleaned_word = re.sub(r"[^\w]", "", word)           # clean the word from special character
        if cleaned_word.lower() == search_word.lower():      # match the word with search_word
            found = True
            break

# print the word existence using conditional statement 
if(found):
    print(f"{search_word} is exists")
else:
    print(f"{search_word} is not exists")