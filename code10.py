rows=int(input("enter input"))
num=1
for x in range(rows):
    num=x+1
    for y in range(rows-x-1):
        print(" ",end="   ")
    for z in range(x+1):
        print(num,end="   ")
        num=num+(x+1)
    print()

