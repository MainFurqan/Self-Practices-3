"""
🔹 Q7: Try–Except–Else–Finally
Task:
Demonstrate usage of:

try

except

else

finally

In a program that takes input, processes it, and always prints "Program finished" at the end.
"""

try:
    # Append user input to the file
    with open("info.txt", "a", encoding="utf-8") as file:
        name = input("Enter your name: ").strip()
        file.write(f"{name}\n")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    # Overwrite file with new input only if no exception occurred above
    with open("info.txt", "w", encoding="utf-8") as file:
        new_name = input("Enter your name again: ").strip()
        file.write(f"{new_name}\n")
finally:
    print("Program finished.")
