data = []

# You can add data of any type to
# a list in Python

data.append(123) # number
data.append("Hi") # string
data.append(1 + 2j) # complex

class C:
    pass
o = C()
data.append(o) # object

for x in data:
    print(x)
    