# Convert strings to integers 
# in one go

data = "10, 20, 30"

strings = data.split(',')
print(strings) # You have strings
               # so far

# We want integers
numbers = list(
    map(int, data.split(','))
    #   ^^^ conversion takes place
    #       here
)
print(numbers)
