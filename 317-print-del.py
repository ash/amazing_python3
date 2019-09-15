# Do not do like this :-)
# This is a bad and dangerous
# practice.

data = [1, 3, 5, 7, 9, 11]
# Let us see why this is bad.

for i in range(len(data)):
    # What is you access an element here?
    print(data[i])
    if i == 3:
        del(data[i])
    # And remove an item from that
    # very list during the "for"
    # loop
print(data)