"""
🔹 Q5: Multiple Exception Types
Task:
Write a program that:

Opens a file

Reads a number from it

Divides 100 by that number

Handle:

FileNotFoundError

ValueError

ZeroDivisionError
Each with appropriate error messages.

"""
try:
    # Write numbers to a file (0 to 9)
    with open("number.txt", "w", encoding="utf-8") as file:
        for i in range(10):
            file.write(f"{i}\n")  # One number per line

    # Read numbers from the file and divide 100 by each
    with open("number.txt", "r", encoding="utf-8") as file_2:
        for line in file_2:
            try:
                number = int(line.strip())  # Remove whitespace/newline
                result = 100 / number
                print(f"100 / {number} = {result}")
            except ValueError:
                print("Invalid number format in file.")
            except ZeroDivisionError:
                print("Cannot divide by zero.")

except FileNotFoundError:
    print("File not found.")

         
