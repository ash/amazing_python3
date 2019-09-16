# Imagine you have a loop over a list
data = [1, 3, 5, 7, 9]

for i in range(len(data)):
# but you want to use indices
    print(data[i])

# Question: how many times does Python
# call "len(data)"? 
# And how many times "range"?