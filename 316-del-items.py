# Do not do like this :-)
# This is a bad and dangerous
# practice.

data = [1, 3, 5, 7, 9, 11]

# You scan along the list
for i in range(len(data)):
    if i == 3:
        del(data[i])
    # And remove an item from that
    # very list during the "for"
    # loop
print(data) # it even works,
# but do not do that