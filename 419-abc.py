import abc

class C(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        pass

class D(C):
    def hello(self):
        print('Hello, I am D')

# c = C()
# c.hello()

# TypeError: Can't instantiate
# abstract class C with abstract
# method hello

d = D()
d.hello()
