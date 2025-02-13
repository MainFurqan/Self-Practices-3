# Define the tuple
tu = (23, "Furqan", 'C')

# Convert the tuple to a list to allow modifications
tu_list = list(tu)

# Remove the element 23
tu_list.remove(23)

# Convert the list back to a tuple
tu = tuple(tu_list)

# Print the modified tuple
print(tu)
