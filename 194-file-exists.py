# How to check if the file 
# or directory exists

import os

print(os.path.exists('data.txt'))
print(os.path.exists('none.txt'))

# also with directories
print(os.path.exists('__pycache__'))