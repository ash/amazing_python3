# What is the length of the string?
# The file is saved as UTF-8

string = '你好，世界！'

print(len(string)) # length in
                   # characters

print(len(string.encode('utf-8')))
# length in bytes (if it is UTF-8)