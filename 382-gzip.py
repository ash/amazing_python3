# Reading gzipped files

import gzip
# A built-in module

# Open the file
with gzip.open('info.txt.gz') as f:
    # Read a byte literal
    str = f.read()
    # Convert to UTF-8 to print
    print(str.decode('utf-8'))
