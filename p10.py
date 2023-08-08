import array
arr=array.array('i',[])
num=int(input("enter no of elements: "))
for i in range(num):
    n=int(input("enter elements: "))
    arr.append(n)
print(arr)
x=0
for x in range(num):

    for i in range(0,x+1,2):            
         temp=arr[x]
         arr[x]=arr[x+1]
         arr[x+1]=temp
        

print(arr)


