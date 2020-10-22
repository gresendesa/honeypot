from bin.encryptor import Honey

h = Honey()

import base64

data = 'Bezouro'
fake = 'ThiagoSá'

key = h.transform(data, fake)

keyencoded = base64.b64encode(str.encode(key))
print(keyencoded)

original = h.reconstruct(fake, key)
print(original)


