class Circle:

    def __init__(self, radius):     # Constructor or init-function
        self.radius = radius
        print("Drawing Circle........")
        print("This is Circle.")

    # Method calculating area of circle
    def area(self):
        pi = 3.14
        a = pi*(self.radius**2)         # applied formula of area of circle
        return a

    # Method calculating perimeter of circle
    def perimeter(self):
        pi = 3.14
        a = (2*pi)*self.radius         # applied formula of perimeter of circle
        return a

# Ask to user enter radius
radius = int(input("Enter radius for Drawing Circle:"))

# Instance of Circle class
c = Circle(radius)            # Entered ' r ' is pass as parameter in constructor 

# Call the method of area 
print("Area of Circle: ", c.area())

# Call the method of Perimeter
print("Perimeter of Circle: ", c.perimeter())