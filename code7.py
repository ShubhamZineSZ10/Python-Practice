rows=int(input("enter input"))
num=9
for x in range(rows):
    for y in range(rows-x-1):
        print("   ",end="        ")
    for z in range(x+1):
        print(num,end="         ")
        num=num+9
    print()

