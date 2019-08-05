# Get the "difference" between the 
# two lists

data1 = [10, 20, 30, 40, 50]
data2 = [5, 10, 15, 20, 25]

diff = list(
    set(data1).symmetric_difference(
        set(data2)
    )
)
print(diff) 
# only elements which are either in
# the first or in the second lists, 
# but not in both