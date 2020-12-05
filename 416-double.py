# The task is to replace spaces
# with double spaces (in a text from
# the file).

# Read the whole text
with open('416.text') as f:
    text = f.read()

# Now, replace spaces with double
# spaces
text = text.replace(' ', '  ')

# And print the result
print(text)
