# Multiple inheritance
class A:
    def a(self):
        print("This is A.a()")

class B:
    def b(self):
        print("This is B.b()")

# Now, create their common child
class C(A, B): # Based on A and B
    pass # let it be empty

obj = C() # Object of class C
obj.a() # can call a method of A
obj.b() # and of B