# Q3: Mixed Argument Display
# Create a function report that accepts:
# One required argument: title
# Any number of *args (comments)
# Any number of **kwargs (meta information)

# Example_function:
# report("Project A", "Good progress", "Need testing", status="In Progress", deadline="Friday")

# Example_Output:
# Title: Project A
# Comments:
# - Good progress
# - Need testing
# Metadata:
# status = In Progress
# deadline = Friday

def report(title, *argu, **key_value):
    print("Title: ", title)

    print("Comments: ")
    for com in argu:
        print(com)
    
    print("Metadata: ")
    for key, value in key_value.items():
        print(f"{key} = {value}")

report("Project_1", "Good progress", "Need Testing", status = "In progress", deadline = "Friday")