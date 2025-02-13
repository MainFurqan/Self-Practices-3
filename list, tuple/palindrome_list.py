# Declare list
list1 = [1, 2, 2, 1]

# Copy the list 
copy_list1 = list1.copy()
reverse_list1 = copy_list1.reverse()  # Reverse the list 

# Check that list is palindrome or not
if(copy_list1 == list1):
    print("list1 is palindrome list")
else:
    print("list1 is not palindrome list")
