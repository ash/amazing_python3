# Implement the "sum" function
# recursively (as an exercise).

def rs(data):
    # data is a list
    if len(data) > 1:
        return data[0] + rs(data[1:])
        #                ^^^
        #    here comes recursion
    else:
        return data[0]

print(rs([4, 5, 7, 9, 10]))