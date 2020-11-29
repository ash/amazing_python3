# Defining custom behaviour for
# the "len" function

class Phrase:
    # our class keeps a phrase
    def __init__(self, text):
        # save it in an object
        self.text = text
    # Let "len" return the number
    # of words in the phrase
    def __len__(self):
        # Count spaces
        return 1 + self.text.count(' ')

# Use the class:
phrase = Phrase("Hello World")
print(len(phrase)) # 2
