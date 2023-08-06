rows=int(input("enter input"))
num=1
for x in range(rows):
    num=1+x
    for y in range(rows-x-1):
        
        print("  ",end=" ")
    for z in range(x+1):
        
        
        if x%2==0:
            print(chr(num+96),end="  ")
            num=num-1
        else:

            print(num,end= "  ")
            num=num-1

    print()

