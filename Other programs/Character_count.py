s = '{} is measured in {}'
print(s.format('Length', 'metres'))
print("""hallo
heimur
hehe  

haha """)
print("hallo heimur hehe haha")

sliced = "hallo heimur"
print(sliced)
sliced = sliced[0:10:2]
print(sliced)


def addone(n):
    n = str(n + "abc")
    return n


num = 10
print(num)
addone(num)
print(num)
