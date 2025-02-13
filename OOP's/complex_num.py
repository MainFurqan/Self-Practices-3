class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img 
    
    def show_num(self):
        return f"{self.real}i + {self.img}j"

    def __add__(self, other):
        if isinstance(other, Complex):
            new_real = self.real + other.real
            new_img = self.img + other.img
            return Complex(new_real, new_img)
        raise TypeError("Operand must be an instance of Complex")
    
    def __str__(self):
        return f"{self.real}i + {self.img}j"

# Example Usage
c1 = Complex(4, 8)
print("First Complex Number:", c1)

c2 = Complex(14, 68)
print("Second Complex Number:", c2)

c3 = c1 + c2
print("Sum of Complex Numbers:", c3)
