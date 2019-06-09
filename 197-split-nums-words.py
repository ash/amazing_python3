# Split a string into numbers
# and words

import re # regular expressions

s = "3 bananas, 15 carrots, 10 apples"

nums = re.findall(r'(\d+)', s)
words = re.findall(r'([a-zA-Z]+)', s)

print(nums)
print(words)