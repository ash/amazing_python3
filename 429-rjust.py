# Using "rjust" to justtify strings
# to the given width

title = 'Quantity'
value1 = 100
value2 = 2456
value3 = 25

width = len(title)
print(title)

print(str(value1).rjust(width))
print(str(value2).rjust(width))
print(str(value3).rjust(width))
