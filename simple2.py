from encryptor import Honey

h = Honey()

import base64

fake = 'ThiagoSá'
key64 = b'EgPvv6/vv7Lvv7Lvv73vv6Q='
key = base64.b64decode(key64).decode()

original = h.reconstruct(fake, key)
print(original)


