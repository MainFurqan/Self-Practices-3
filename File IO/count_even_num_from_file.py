import re

# Define fun for count of even_num from file
def count_even_num(address_file):
    count = 1
    with open(address_file, "r") as fr:
        for digit in fr.read().split():    # split content into digit
            cleaned_digit = re.sub(r"[^\w]", "", digit)           # clean the digit from special character
            cleaned_digit = int(cleaned_digit)
            if (cleaned_digit%2 == 0):      # check that given digit is even or odd
                count += 1
                print(cleaned_digit)
    return count

# Call  the function with passing address of my file
print(count_even_num("numeric_number.txt"))