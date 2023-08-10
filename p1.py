""" 
Accessing parent's class variable from child class
when both are initialised with same name

"""
class Parent:
    x="ParentClassVar"
    def __init__(self):
        print("In Parent const.")
        self.y="ParentInstVar"

    def disp(self):
        print(self.y)

    @classmethod
    def show(cls):
        print(cls.x)

class Child(Parent):
    x="ChildClassVar"
    def __init__(self):
        super().__init__()
        print("In Child const.")
        self.a="ChildInstVar"

    def dispc(self):
        print(self.a)

        

    @classmethod
    def showc(cls):
        print(cls.x)
        print(super().x)
    
obj=Child()
obj.dispc()
obj.disp()
obj.showc()



