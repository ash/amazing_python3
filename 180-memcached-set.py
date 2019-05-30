# Using memcached to exchange data
# between processes

from pymemcache.client import base
# to install run:
# pip3 install pymemcache

client = base.Client(
    ('localhost', 11211) # default port
)

client.set('my_data', 'Hello, World!')
