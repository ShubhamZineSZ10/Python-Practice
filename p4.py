""" 
Static Method"""
class Cric:
    format="T20"

    def __init__(self):
        print("in const.")
        self.name="Dhoni"
        self.jer=7

    @classmethod
    def dispData(cls):
        print("in class method")
        cls.format="odi"

    def printData(self):
        print("in instance method")
        print(self.name)
        print(self.jer)
        self.format="test"

player1=Cric()
player2=Cric()

print(player1.format)
print(player2.format)

player1.printData()
print(player1.format)
print(player2.format)

player2.dispData()
print(player1.format)
print(player2.format)

class BCCI:
    @staticmethod                    #static method is used to make change in 1st class's method by usind the object of that class in 2nd class
    def laksh(player2):
        player2.jer=0

shah=BCCI()
shah.laksh(player2)
player2.printData()

player1.printData()






















