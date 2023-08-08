import array
arr=array.array('i',[])
num=int(input("enter no of elements: "))
for i in range(num):
    n=int(input("enter elements: "))
    arr.append(n)
print(arr)
y=int(input("Occurrence count of a number: "))
print(arr.count(y))
    

