# CREATING OBJECT 

class Dog:

    def __init__(self,name,age):
        print("In constructor..")
        self.name=name
        self.age=age
        
        
    def walk(self):
        print("In walk function..")
        print("name", self.name)
        print("age", self.age)
Lebra = Dog("Tommy",5)
Pam = Dog("Harry",12)

Lebra.walk()
Pam.walk()
print(Lebra.name)
print(Pam.name)
