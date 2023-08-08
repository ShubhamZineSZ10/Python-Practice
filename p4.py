import array
arr=array.array('i',[])
sum=0
num=int(input("enter no of elements: "))
for i in range(num):
    n=int(input("enter elements: "))
    arr.append(n)
print(arr) 
for i in arr:
    if (arr.index(i))%2==0:
        sum=sum+i
print(sum)        
