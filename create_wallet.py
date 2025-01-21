#!/usr/bin/env python3
from tronpy.keys import PrivateKey

wallet = PrivateKey.random()

with open("secret_key.txt", "w") as secret_key_file:
    secret_key_file.write(f'{wallet}')

print("Paper wallet created and secret key saved.")
