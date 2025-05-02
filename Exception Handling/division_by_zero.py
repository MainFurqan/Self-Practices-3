"""
🔹 Q2: Division by Zero
Task:
Ask the user to input two numbers and perform division.

Handle the case where the denominator is zero and display a message:
"Cannot divide by zero!"

🔹 Q3: Valid Integer Input
Task:
Ask the user to enter their age.

Use exception handling to catch non-integer input.

Print "Please enter a valid integer." if the input is not an integer.
"""

while True:
    try:
        print("\n Perform Division:")
        print("Enter whole numbers only.")
        
        num_1 = int(input("Enter num_1: "))
        num_2 = int(input("Enter num_2: "))
        
        division = num_1 / num_2
        print(f" Output: {num_1} / {num_2} = {division}")
        break  # Exit loop if division is successful

    except ZeroDivisionError:
        print(" Cannot divide by zero! Please try again.")
        continue  # Ask again

    except ValueError:
        print(" Please enter a valid whole (integer) number.")
        continue  # Ask again
