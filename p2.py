import array
arr=array.array('I',[])
num=int(input("enter no of elements: "))
for i in range(num):
    n=int(input("enter the element: "))
    arr.append(n)

print(arr)

for x in arr:
    if x%2!=0:
        print(x)

