# Write numbers from 1 to 100 into a file, separated by commas

with open("numeric_number.txt", "w") as file:
    # Generate a comma-separated string of numbers
    numbers = ", ".join(map(str, range(1, 101)))
    file.write(numbers)

print(f"Numbers 1 to 100 have been written to {output_file}.")
