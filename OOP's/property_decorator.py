class student:
    def __init__(self, math, phy, chem):
        self.math = math
        self.phy = phy
        self.chem = chem

    @property
    def cal_percentage(self):
        return str((self.math + self.phy + self.chem)/3) + "%"

    def update_per(self):
        return str((self.math + self.phy + self.chem)/3) + "%"

s1 = student(99, 88, 77)
# print(s1.update_per())
print(s1.cal_percentage)

s1.math = 87
#print(s1.update_per())
print(s1.cal_percentage)