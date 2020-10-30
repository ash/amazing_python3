# Using a lambda function in 
# a filter. Let's print the numbers
# whose absolute value is > 3.

data = 2, -3, 1, 4, 5, -6, 10, -2

res = list(
    filter(
        lambda x: abs(x) > 3,
        data
    )
)
print(res)
