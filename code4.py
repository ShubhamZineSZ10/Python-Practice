rows=int(input("enter the input"))

for x in range(rows):
    num=rows-x
    for y in range(rows-x):
        print(chr(num+96),end=" ")
        num=num-1
    print()


