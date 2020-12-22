# List all files (and directories)
# in the current directory

import os

# '.' is the current directory
for name in os.listdir('.'):
    print(name)
