rows=int(input("enter the input"))
num=rows
for x in range(rows):
    num=rows-x
    
    for y in range(rows-x):
        
        if x%2!=0:

            print(chr(num+64),end=" ")
            num=num-1
    
        else:
        
            print(num,end=" ")
            num=num-1
         
        
    print()
    

    


