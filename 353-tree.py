# Let's print a tree
# and make it symmetric

for i in range(1, 20, 2):
    # loop with the step of 2
    print(('*' * i).center(20))
    # double () are to call
    # .center on a string,
    # not on the result of "print"

# * repeats a string i times