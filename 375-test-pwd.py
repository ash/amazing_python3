# Test if the password has small
# and big letters and digits

import re

pwd = 'HelloW0rl1d'
if re.search('[a-z]', pwd) and \
    re.search('[A-Z]', pwd) and \
    re.search('\d', pwd):
    print('Good')
else:
    print('Bad')
