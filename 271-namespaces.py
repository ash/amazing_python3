# Exploring namespaces

print(dir()) # You are in __main__ now

def f():
    x = 42
    print(dir()) # Inside f()

f()

# Compare the output of these
# two dir() calls