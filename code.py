rows=int(input("enter the input: "))

for x in range(rows):
    num=rows
    for y in range(rows):
        print(chr(64+num),end="")
        print(num,end=" ")
        num=num-1
    print()


