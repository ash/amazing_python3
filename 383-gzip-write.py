# Let's create a .gz file and write to it

import gzip

with gzip.open('test.txt.gz', 'wb') as f:
    # wb = write, binary
    f.write(b'Hello there!\n')
    f.write(b'Here is out text\n')
