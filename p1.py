""" Objects of same class have different address,
it means there are two different namespaces formed"""


class IPL:
    teams=10
    format="t20"

    def match(self):
        print("csk vs mi")


obj1=IPL()
obj2=IPL()
print(obj1)
print(obj2)
print(obj1.__class__)
print(obj2.__class__)
