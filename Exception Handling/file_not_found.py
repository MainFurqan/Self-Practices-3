"""
🔹 Q1: File Not Found
Task:
Write a program to open a file named report.txt.

If the file does not exist, catch the exception and print:
"File not found. Please check the file name."

"""

try:
    with open("report.txt", "r") as file:
        print("File is open......")
except FileNotFoundError:
    print("File not found. Please check the file name.")
