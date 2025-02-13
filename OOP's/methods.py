class Group:
    gro_name = 'A'

    # Static Method
    def greet(gro_name):
        print(f"Welcome {gro_name}")

    # Instance method 
    def chan_nam(self, name):
        self.gro_name = name

    # class method
    @classmethod
    def change_name(cls, g_name):
        cls.gro_name = g_name

g1 = Group()
g1.chan_nam("F")
print(g1.gro_name)
print(Group.gro_name)