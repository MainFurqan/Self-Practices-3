class Employee:
    def __init__(self, role, depart, salary):
        self.role = role
        self.depart = depart
        self.salary = salary
 
class Engineer(Employee):
    def __init__(self, name, age, role, depart, salary):
        super().__init__(role, depart, salary)
        self.name = name
        self.age = age

    # Method for showing Intro
    def show_intro(self):
        print(self.name)
        print(self.age)
        print(self.depart) 
        print(self.role)
        print(self.salary)


# Instance of Employee class    
en1 = Engineer("Furqan", 20, "Engineer", "CS", "1Lack")
print(en1.show_intro())       # Calling the show_intro method