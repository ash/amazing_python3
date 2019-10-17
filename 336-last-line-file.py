# Reading the last line from a file

import os 
with open('lines.txt') as f:
    # Go to the last character
    last = f.seek(0, os.SEEK_END)
    while last: # while last != 0
        last = last - 1
        f.seek(last)
        if f.read(1) == "\n":
            # Found the first newline
            # character from the 
            # end of file
            print(f.readline())
            # Read the rest from
            # that position
            break