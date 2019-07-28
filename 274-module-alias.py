# Importing a module and giving it
# an alias

# Now change the name:
import random as r
# From this moment, you need to
# use the new alias in your program

# So this will not work:
# print(random.randint(10, 20))

# This will work:
print(r.randint(10, 20))
#     ^ using the alias
