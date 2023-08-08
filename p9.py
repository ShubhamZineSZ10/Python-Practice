import array
arr=array.array('i',[])
num=int(input("enter no of elements: "))
for i in range(num):
    n=int(input("enter elements: "))
    arr.append(n)
print(arr)
count=0
for x in range(len(arr)):
    for y in range(x+1,len(arr)):
        if arr[x]==arr[y]:
            print(arr[y])

    

    
    


