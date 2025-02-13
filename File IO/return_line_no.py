# Define the function for word-found-line-no
def search_line_no(search_word):
    line_no = 1
    
    with open("practice.txt", "r") as f:
        for line in f:
            line_no += 1
            if search_word in line:
                print("Found at line")
                return line_no
    return -1
    
# Ask to user enter input    
search_word = input("Search here........")
# Call the function
print(search_line_no(search_word))