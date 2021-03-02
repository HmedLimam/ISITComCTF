# Title: Fruit

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

def encrypt(text):
    BLOCK_SIZE = 32
    key = "cherry".zfill(8).encode()
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(text, BLOCK_SIZE)
    return b64encode(des.encrypt(padded_text))[::-1]

# cipher = b'==gQpiM4fhGYaIUqID+XoBmGClKyg/FagpBOgWglc36yiFx6Ksx5i5mnD0q2e+0efs4VchhVuSscaTyzUkVTSE1Q'

def decrypt(encrypted_text, key):
    BLOCK_SIZE = 32
    key = key
    des = DES.new(key, DES.MODE_ECB)
    return unpad(des.decrypt(encrypted_text), BLOCK_SIZE)


fruits = ["Apple", "Apricot", "Banana", "Cherry", "Fig", "Orange", "Pear"]

for fruit in fruits:
    try:
        print(decrypt(b64decode(
            b'==gQpiM4fhGYaIUqID+XoBmGClKyg/FagpBOgWglc36yiFx6Ksx5i5mnD0q2e+0efs4VchhVuSscaTyzUkVTSE1Q'[::-1]),
                      fruit.lower().encode().zfill(8)), fruit)
    except:
        continue
