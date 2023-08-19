# HOW TO REVERSE A STRING

# SLICING
string1="shubham"
print(string1[::-1])

# REVERSED()
string1="".join(reversed(string1))
print(string1)

#USING FOR LOOP
string2="Vishal"
def reverse(str):
    s=""
    for i in str:
        s=i+s
    return s
print("Reversed: ",reverse(string2))

#USING RECURSION
string3="Akash"
def reverse1(str):
    if len(str)==0:
        return str
    else:
        return reverse1(str[1:])+str[0]
print("Reversed : ",reverse1(string3))
