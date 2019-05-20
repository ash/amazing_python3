# The "for" loop can have an
# "else" clause

for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print('done') # printed after
    # the end of the loop
    # but only if the loop finished
    # successfully