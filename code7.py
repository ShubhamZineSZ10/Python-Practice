num=(input("enter the input")

if (chr(num)>="A" and chr(num)<="Z") or (chr(num)>"=a"and chr(num)<="z"):
    print("it is an alphabet")
    
elif type(num)==int:
    print("it is digit")
else:
    print("special character")

