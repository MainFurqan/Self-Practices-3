# Ask to user enter obtained marks
obtain_m = float(input("Obtained Marks: "))
# Ask to user enter Total marks
Total_m = float(input("Total Marks: "))

# Validation of entered marks
if(obtain_m > Total_m):
    print("Error: your obtain marks greater than total marks.")
else:
    # Calculate the percentage
    per = (obtain_m/Total_m)*100

    # Determine the Grade based on percentage
    if 90 <= per <= 100:
        grade = "A+"
    elif 80 <= per < 90:
        grade = "A"
    elif 70 <= per < 80:
        grade = "B"
    elif 60 <= per < 70:
        grade = "C"
    elif 50 <= per < 60:
        grade = "D"
    elif 40 <= per < 50:
        grade = "E"
    else:
        grade = "F"
    
    # Display the result
    print(f"Percentage {per}%")
    print(f"Grade {grade}")