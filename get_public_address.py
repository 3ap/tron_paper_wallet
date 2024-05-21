from tronpy import Tron, keys

secret_key = ''
with open("secret_key.txt", "r") as secret_key_file:
    secret_key = secret_key_file.read().strip()

if secret_key:
    wallet = keys.PrivateKey(bytes.fromhex(secret_key))
    public_address = wallet.public_key.to_base58check_address()
    print("Public TRON address:", public_address)

