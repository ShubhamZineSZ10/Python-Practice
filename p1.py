tuple1 = (1,2,3,"ajay","om",4)
print(str(tuple1))
print(tuple1[1])
print(tuple1[4])
print(tuple1[-1])
tuple2=("erg","fgt",5,8,6,0)
print("tup2",tuple2)
tuple3 = tuple1+tuple2
print("tup3",tuple3)
tuple4=sum((tuple1,tuple2),())
print(tuple4)
tuple1=list(tuple1)
tuple1.clear()
print(tuple1)
tuple2=tuple2[0:0]
print(tuple2)

