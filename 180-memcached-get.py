# Using memcached to exchange data
# between processes

from pymemcache.client import base
# to install run:
# pip3 install pymemcache

client = base.Client(
    ('localhost', 11211) # default port
)

my_data = client.get('my_data')
print(my_data)

