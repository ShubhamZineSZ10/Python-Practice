"""
    CLASS METHOD"""


class Cric:
    format="T20"
    def __init__(self,name,jerNo):
        self.name=name
        self.jerNo=jerNo

    def Inst(self):
        print("IN Instance method")
        print(self.name)
        print(self.jerNo)
        print(self.format)
        print(self)                             #self and obj1 gives the same address it means obj1 is passed to the self
        
    @classmethod
    def Class(cls):
        print("In Class method")
        print(cls.format)            # class method is used to access class method
       # print(cls.name)             #class method can not access instance variable
        
obj1=Cric("dhoni",7)
obj1.Inst()
obj1.Class()
Cric.Class()                         #class method can be accessed through both object as well as class
#Cric.Inst()                         #but instance method is only accessed with the object not with the class name


print(obj1)               #object of a class
print(Cric)               # class


