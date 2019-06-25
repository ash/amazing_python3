# UUID v1 vs. UUID v4

import uuid

for _ in range(5):
    print(uuid.uuid1())

print('')

for _ in range(5):
    print(uuid.uuid4())
