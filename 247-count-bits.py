# Count bits "1" in a binary 
# representation of a positive
# integer number

num = 12345
bin_num = bin(num) # this is 
# a string, let's see it:
print(bin_num)

# Now count the "1"s:
c = bin_num.count('1')
print(c) # the number of 1 bits