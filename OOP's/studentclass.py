# create student class
class Student:
     def __init__(self, name, sub1, sub2, sub3):    # parametrize Init_function or parametrize constructor
          self.name = name
          self.sub1 = sub1
          self.sub2 = sub2
          self.sub3 = sub3


     # Method for calculation of Average 
     def average(self):
          ave = (self.sub1 + self.sub2 + self.sub3)/3
          return ave

# 's1' is object
s1 = Student("ALI", 97, 90, 92)
print(s1.average())             # call the average method
     