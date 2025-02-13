class Student:
    def __init__(self, level):
        self.level = level

class Intro(Student):
    def __init__(self, name, level):
        self.name = name
        super().__init__(level)

s1 = Intro("Ali", 9)
print(s1.name)
print(s1.level)