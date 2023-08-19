#AMSTRONG NUMBER
num=int(input("Enter the no: "))
temp=num
count=0
while(temp>0):
    count +=1
    temp=temp//10
temp=num
sum=0
while temp>0:
    rem=temp%10
    sum=sum+(rem**count)
    temp=temp//10
if(sum==num):
    print("Num is Amstrong..")
else:
    print("Num is not Amstrong..")

