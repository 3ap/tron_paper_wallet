#!/usr/bin/env python3
from tronpy.keys import PrivateKey
from tronpy.hdwallet import TRON_DEFAULT_PATH, generate_mnemonic, key_from_seed, seed_from_mnemonic

mnemonic = generate_mnemonic(12, "english")
seed = seed_from_mnemonic(mnemonic, passphrase="")
key = key_from_seed(seed, TRON_DEFAULT_PATH)
wallet = PrivateKey(key)

with open("secret_key.txt", "w") as secret_key_file:
    secret_key_file.write(f'{wallet}\n')
with open("mnemonic.txt", "w") as mnemonic_file:
    mnemonic_file.write(f'{mnemonic}\n')

print("Paper wallet created and secret key saved.")
