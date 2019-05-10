# How to push data to a list
# and how to pop it back

data = []

for i in range(5):
    data.append(i * i)
    # fill with some data

while(len(data)):
    # while list is not empty
    value = data.pop() # take from
                       # back
    print(value)
# Printed in reverse order