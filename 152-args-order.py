# *args should be at the end
# of the list of arguments

def print_powers(pwr, *values):
    for v in values:
        print(v ** pwr)

print_powers(2, 3, 5, 7)
print_powers(3, 3, 5, 7)