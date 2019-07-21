# Currying in Python

# What you want to achieve:
# result = a(3)(4)

def a(x):
    def b(y):
        return x + y
    return b # name of function

result = a(3)(4)
print(result) # 7, for example