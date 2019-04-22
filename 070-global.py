# The "global" keyword

n = 1

def inc_n():
    global n
    n += 1 # this one

print(n) # 1
inc_n()
print(n) # 2
