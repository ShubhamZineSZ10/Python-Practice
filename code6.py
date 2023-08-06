a=int(input("enter value of a"))

b=int(input("enter the value of b"))

c=int(input("enter the value of c"))

if (c*c)==(a*a)+(b*b):
    print("Pythagorean triplet")
elif (a*a)==(c*c)+(b*b):
    print("Pythagorean triplet")
elif (b*b)==(c*c)+(a*a):
    print("Pythagorean triplet")
else:
    print("not a pythagorean triplet")

    
