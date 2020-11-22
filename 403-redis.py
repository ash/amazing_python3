# Using Redis
import redis

# Connect to the local service
r = redis.Redis()

# Set a key
r.set('my:key', 'My first value')

# Read the value at that key
val = r.get('my:key')

# Print it
print(val) # a bytestring btw
