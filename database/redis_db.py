"""Basic connection example.
"""

import redis

r = redis.Redis(
    host='lively-place-accordant-94048.db.redis.io',
    port=12561,
    decode_responses=True,
    username="default",
    password="i4uayy74roSv8WRrp72bTzWp0fhCYDYi",
)

success = r.set('foo', 'bar')
# True

result = r.get('foo')
print(result)
# >>> bar

