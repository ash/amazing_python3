# Matching more than one number

import re

date = '2019-04-21'
match = re.search(
    '(\d+)-(\d+)-(\d+)', date)
if match:
    print(match.groups())
    # this is a tuple:
    print(type(match.groups()))
