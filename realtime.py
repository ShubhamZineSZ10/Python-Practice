class Company:
    cname="Veritas"
    workplace="Baner"

    def __init__(self):
        print("Company Constructor")
        self.teamcode="Python Code"

    @classmethod
    def facilities(cls):
        print("Provides all facilities...")
        print(cls.name)
        print(cls.workplace)

    def compInfo(self):
        print(self.teamcode)

class Employee(Company):
    role="Developer"

    def __init__(self,empId,name):
        super().__init__()
        print("Child Constructor")
        self.empId=empId
        self.name=name

    def empInfo(self):
        print(self.empId)
        print(self.role)
        print(self.name)
        print(self.workplace)
        print(".............................................")

    @classmethod
    def skillset(cls):
        print(cls.role)

emp1=Employee(11,"Raj")
emp2=Employee(21,"Suraj")
print("Before any change........... ")
emp1.empInfo()
emp2.empInfo()

emp1.workplace="Hadapsar"
print("After change in emp1 workspace to Hadapsar......")
emp1.empInfo()
emp2.empInfo()
Company.workspace="Banglore"
print("After change in Company workspace to Banglore......")

emp1.empInfo()
emp2.empInfo()

print(Company.workspace)
print(Employee.workspace)
print(emp1.workspace)
print(emp2.workspace)
"""
emp1.workspace="Banglore"
print("After changing the emp1 to Banglore")

emp1.empInfo()
emp2.empInfo()
print(emp1.workspace)
print(emp2.workspace)

Company.workspace="Delhi"
print("After changing Company workspace to delhi......")

print(Company.workspace)
print(Employee.workspace)
print(emp1.workspace)
print(emp2.workspace)




"""





