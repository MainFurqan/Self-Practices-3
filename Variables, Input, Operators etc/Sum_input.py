try:
    # Ask to user enter the two number for calculation of their sum
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))

    # Calculate the sum
    sum = num_1 + num_2

    # Display the output
    print(f"{num_1} + {num_2} = {sum} ")
except ValueError:
    print("Invalid input: Please enter numeric number.")