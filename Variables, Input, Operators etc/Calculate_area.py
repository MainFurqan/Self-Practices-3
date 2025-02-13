try:
    # Ask to user enter the side length of square
    side = float(input("Enter the length of a side of the square: "))
    # calculation of Area of the square
    Area = side**2    
    # Display the output
    print(f"Area of the square is {Area}")
except ValueError:
    print("Please enter numeric number.")