# What are all those __add__ etc about?

# Imagine two numbers, you can add
# them up:
print(3+4)

# For doing the same with objects,
# you have to implement the behaviour
# of "+" for them
class C:
    def __add__(a, b):
        return 42 # Let it be a constant

# Imagine now two objects:
o1 = C()
o2 = C()

# And you also want to add them up:
print(o1 + o2) # the __add__ method
               # is called here
