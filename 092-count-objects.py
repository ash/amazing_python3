# Counting objects

class Item:
    counter = 0

    def __init__(self):
        Item.counter += 1
        self.counter = Item.counter

    def my_number(self):
        return self.counter

for _ in range(5):
    objectN = Item()
    print('My number is ' + str(
        objectN.my_number()
    ))