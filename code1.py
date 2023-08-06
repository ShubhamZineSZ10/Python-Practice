rows=int(input("enter the input"))

num=1
for x in range(rows):
    num=x+1
    for y in range(rows):
        print(num,end=" ") 
        sum=num+3
        num=sum
    print() 

