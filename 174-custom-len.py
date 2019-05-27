class C:
    def __init__(self, str):
        self.data = str
    def __len__(self):
        return len(self.data)

c = C('Hello')
print(len(c))
