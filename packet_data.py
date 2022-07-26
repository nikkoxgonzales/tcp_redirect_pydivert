from struct import *

data = b'3\x039'
d = unpack("V", data)
print(d)