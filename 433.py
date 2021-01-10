# Create a dictionary

d = {'a' : 100, 'b' : 200}

# Add a new element
# d['c'] = 300
# But by mistake, you type this:
d['c'] : 300 # This is incorrectly
# used type annotation (type hint)

# As in
s: str = 'hello'

print(__annotations__)

print(d) # What will be printed?
