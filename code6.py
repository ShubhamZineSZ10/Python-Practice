rows=int(input("enter the input"))
num=1

for x in range(rows):
    for y in range(x+1):
        num=1
        num=num+x
        if y%2==0:
            data=chr(65+x)
            print(data,end=" ")
            
        else:
            print(num,end=" ")
            
         
    print()






