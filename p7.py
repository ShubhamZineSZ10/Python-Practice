import array
arr=array.array('i',[])
num=int(input("enter the number of elements: "))
for i in range(num):
    n=int(input("enter elements: "))
    arr.append(n)
print(arr)
x=int(input("Search: "))
print(arr.index(x))

