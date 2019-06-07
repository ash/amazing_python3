# Polymorphism in Python

class Animal:
    def talk(self):
        print('I am an animal')
class Dog(Animal):
    def talk(self):
        print('I am a dog')
class Cat(Animal):
    def talk(self):
        print('I am a cat')

# Now make a list with objects of different
# classes from the above defined
zoo = [Dog(), Dog(), Cat(), Animal(), Cat()]

# And iterate over them:
for x in zoo:
    x.talk() # Which "talk" method is called?