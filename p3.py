import array
arr=array.array('I',[])
num=int(input("enter no of elements: "))
for i in range(num):
    n=int(input("enter elements: "))
    arr.append(n)
print(arr)

for ele in arr:
    flag=0
    for x in range(2,ele):
        if ele%x==0:
            flag=flag+1
    if flag==0:
        print(ele)

