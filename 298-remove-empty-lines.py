# Remove empty lines from a text file
# and print the result

with open('text2.txt') as f:
    # loop along the file
    for line in f:
        # if there are any non-space
        # characters
        if line.strip():
            # then print the line
            print(line, end='')
            # and do not add \n
