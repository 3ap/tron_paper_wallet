#!/usr/bin/env python3
from tronpy.keys import PrivateKey
from tronpy.hdwallet import TRON_DEFAULT_PATH, key_from_seed, seed_from_mnemonic

mnemonic = input("Please type your mnemonic words: ")
seed = seed_from_mnemonic(mnemonic, passphrase="")
key = key_from_seed(seed, TRON_DEFAULT_PATH)
wallet = PrivateKey(key)

with open("secret_key.txt", "w") as secret_key_file:
    secret_key_file.write(f'{wallet}\n')

print("Paper wallet recovered secret key saved.")
