# The "id" function

class C:
    pass

# Let's create two objects:
o1 = C()
o2 = C()

# And a variable poiting to one of them:
o3 = o2

# Now let's see at their ids:
print(id(o1)) # an object
print(id(o2)) # a different object
print(id(o3)) # same object as o2