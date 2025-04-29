# Q2: Show Student Info using **kwargs
# Write a function student_info that takes any number of keyword arguments and prints them in the format:
# Such as:
# name = Alice
# age = 20
# course = Python
# Example:
# student_info(name="Alice", age=20, course="Python")

# Defining the function 
def student_info(**key_value):
    for key, value in key_value.items():
        print(f"{key} = {value}")

# Calling the function
student_info(name= "Furqan", Student = "BSCS", age = 20)
