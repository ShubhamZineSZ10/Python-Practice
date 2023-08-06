rows=int(input("enter the input"))
num=0
for x in range(rows):
   # num=0
    for y in range(rows):

        if (x+y)%2==0:
            
            
            print(chr(65+num),end=" ")
            num=num+1
        else:
            print(chr(97+num),end=" ")
            num=num+1 
            
    print()
    

