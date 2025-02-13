# Tuple of numbers
tup = (1, 4, 9, 16, 25, 36, 45, 99, 222, 567)

# Ask the user to enter a number to search
n = int(input("Enter a number to search: "))


for i in range(len(tup)):
    if(tup[i] == n):        # indexed value match with search n
        found = True
        break      

if(found):
    print(f"{n} is exist")
else:
    print(f"{n} is not exist")



# " Below if statement is built-in"
# Check if the number exists in the tuple
# if n in tup:
#    print(f"{n} exists in the tuple.")
# else:
#    print(f"{n} does not exist in the tuple.")