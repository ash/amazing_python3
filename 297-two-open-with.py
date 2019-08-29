# You can open more than one file
# within a single "with":

# Open a.txt for reading,
# Open b.txt for writing ('w')
with \
    open('a.txt') as a, \
    open('b.txt', 'w') as b:
    # For each line in a.txt
    for line in a:
        # copy it to b.txt
        b.write(line)
