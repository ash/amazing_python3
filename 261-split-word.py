# Two methods to split a word
# into separate letters

word = 'Hello'

letters1 = list(word) # converts to
# a list

letters2 = [ch for ch in word] 
# list comprehension

print(letters1)
print(letters2)
