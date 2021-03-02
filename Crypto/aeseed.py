# The whole point is that the key used for AES encryption is randomly generated but the possibilities aren't infinite!
# seed = random.randrange(0,256)
# We can easily try decrypting the ciphertext with every key created with numbers ranging from 0 to 256.

from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import random

flag = b"TODO"

def pad(msg):
  while(len(msg) % 16 != 0):
    msg += b'\x00'
  return msg

def getRandomBytes(seed):
  random.seed(seed)
  key = long_to_bytes(random.getrandbits(8*16))
  return key

def enc(flag):
  seed = random.randrange(0,256)
  key = getRandomBytes(seed)	# generate random 16 bytes
  flag = pad(flag)
  aes = AES.new(key, AES.MODE_ECB)
  cipher = aes.encrypt(flag)
  print(b64encode(cipher))

# FOfO+64HpIW66Nr6NW7exOhDHrP5D7wNMtf/0AxlUr08robiXC6HFurF6aYCNVRM

def dec(cipher, seed):
  key = getRandomBytes(seed)
  aes = AES.new(key, AES.MODE_ECB)
  cipher = b64decode(cipher)
  new = aes.decrypt(cipher)
  return new

for i in range(256):
  try:
    print(dec("FOfO+64HpIW66Nr6NW7exOhDHrP5D7wNMtf/0AxlUr08robiXC6HFurF6aYCNVRM", i).decode(), i)
  except:
    continue
    
# inf{s33d_isn't_as_secure_as_you_think_it_is}
