# Using map comprehensions

ascii = {
    # Let's make a dictionary
    # with the ASCII table
    i: chr(i) for i in range(32, 127)
}
# i: chr(i) = key: value

print(ascii)
