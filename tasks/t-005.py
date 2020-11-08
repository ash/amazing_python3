word_a = 'hello'
word_b = 'world'

# Sets of letters in the words;
# each letter appears only once
in_a = set(word_a)
in_b = set(word_b)

# Difference between the two sets
common = in_a.intersection(in_b)

# Also works for this task:
# common = in_b.intersection(in_a)

# Print common letters
print(common) # {'l', 'o'}
