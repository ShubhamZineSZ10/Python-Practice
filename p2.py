"""
    INSTANCE VARIABLE AND INSTANCE METHOD """
                                             
 

class Class:
    x=10
    def __init__(self):
        print("In Constructor")
        self.a=1
        self.b=2

    def Inst(self):
        print("In Static method")
        print(self.a)
        self.c=3
        print(self.c)

obj1=Class()
obj1.Inst()
print(obj1.b)     
print(obj1.x)     #class variable can be called with the object as object namespace contains a copy of class variables
print(Class.x)    #class variable can be called with class name

obj2=Class()
obj2.Inst(

        )
print(obj1)
print(obj2)
