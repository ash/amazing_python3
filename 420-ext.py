# Extracting an extension from
# a filename

# E.g.: text123.txt => txt

filename = 'text123.txt'

# Split by "." and take the last part
ext = filename.split('.')[-1]

print(ext) # txt
