try:
    # Ask to user enter two number for calculation of their average 
    num_1 = float(input("Enter first number: "))
    num_2 = float(input("Enter Second number: "))

    # Calculate average
    avg = (num_1 + num_2) / 2

    # Display the output
    print(f"The average of {num_1} and {num_2} is {avg}")
except ValueError:
    print("Invalid input: Please Enter numeric input.")