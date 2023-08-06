num1=int(input("enter no.1"))
num2=int(input("enter no. 2"))
num3=int(input("enter no. 3"))
if num1<num2 and num1<num3:
    print(num1,"is min")
elif num2<num1 and num2<num3:
    print(num2,"is min")
else:
    print(num3,"is min")

