# Declare the empty dictionary for store subject wise marks
marks = {}

# Get the number of subject from student.
n = int(input("How many subject of you?"))

# Using loop get subject name and marks from student of all subject  
for i in range(1, n+1):
    key = input(f"Subject Name#{i}: ")
    marks[key] = float(input("marks: ")) 

print(marks) # Display the all subject with marks
