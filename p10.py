#STRONG NUMBER
num=int(input("Enter the number: "))
sum=0
temp = num
while temp>0:
    rem=temp%10
    fact=1
    for i in range(1,rem+1):
        fact *=i
    sum=sum+fact
    temp=temp//10
if(sum == num):
    print("Strong Number..")
else:
    print("Not a Strong number..")
