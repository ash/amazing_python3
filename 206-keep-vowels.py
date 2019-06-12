# Take a strign. Remove all character
# that are not vowels. Keep spaces
# for clarity

import re # regular expressions

s = 'Hello, World! This is a string.'

# sub = substitute
s2 = re.sub(
    '[^aeiouAEIOU ]+', # vowels and 
    # a space
    '', # replace with nothing
    s
)
print(s2)