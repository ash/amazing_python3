# How to get file size in bytes

import os

statinfo = os.stat('data.txt')
print(statinfo.st_size)
