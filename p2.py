class Byjus:

    founder="Ravindran Byju"
    
    def __init__(self):
    
        self.myCourses=5
        self.myMarks=89

    def myReport(self):

        print("Byjus Student Info")
        print(self.myCourses)
        print(self.myMarks)

    @classmethod
    def demoLectures(cls):
        print(cls.founder)

class Akash(Byjus):
    
    def __init__(self):
        
        super().__init__()
        
        self.teachers=100
        self.revenue="2.5 B$"

    def management(self):

        print("Akash's Info")
        print(self.teachers)
        print(self.revenue)
           

Obj1=Akash()
Obj1.management()
Obj1.myReport()
Obj1.demoLectures()
Obj1.founder="asdf"
print(Obj1.founder)

Obj1.demoLectures()


