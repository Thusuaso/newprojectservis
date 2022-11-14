
import hashlib
import base58
import binascii
import random

def get_binary_hex():
    rakam = range(2)

    str_binary = ""
    for i in range(1,257):
        str_binary += str(random.choice(rakam))
    
    return f"{int(str_binary,2):X}"



for i in range(0,10):

    print(get_binary_hex())





