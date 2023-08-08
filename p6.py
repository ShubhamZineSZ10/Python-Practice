import array
arr=array.array('i',[])
num=int(input("enter no of element: "))
for i in range(num):
    n=int(input("enter elements: "))
    arr.append(n)
print(arr)
print("Maximum is: ",max(arr))
print("Minimun is: ",min(arr))

