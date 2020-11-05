# Using "slice objects"
# Did you know that you can save
# a slice in a variable?

txt = 'Hello, Great World!'

my_slice = slice(3, 10)
print(txt[my_slice])

txt = 'Another string to be sliced'
print(txt[my_slice])
