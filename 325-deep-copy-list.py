# Copying lists with elements which
# are objects (instances of a class)

class C:
    def __init__(self, v):
        self.value = v
    def set(self, v):
        self.value = v

data = [C(7), C(8)]
data2 = data.copy() # A copy? Yes, but

data2[0].set(11) 

print(data[0].value)  # also 11
print(data2[0].value) # 11