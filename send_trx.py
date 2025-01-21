#!/usr/bin/env python3
from tronpy import Tron, keys
from tronpy.providers import HTTPProvider

def trx_to_sun(trx_amount):
    return int(trx_amount * 1000000)

api_key="03f17615-a928-4406-bc14-ad61373427ef" # Get it from https://www.trongrid.io/dashboard
to_address = "TNuTtmTdmdGWKQSnySroeXjyzGh1ZsRau2" # Where you want to send your TRX
amount = trx_to_sun(1.19)  # The amount of TRX to send

secret_key = ''
with open("secret_key.txt", "r") as secret_key_file:
    secret_key = secret_key_file.read().strip()

tron = Tron(HTTPProvider(api_key=api_key))

if secret_key:
    try:
        wallet = keys.PrivateKey(bytes.fromhex(secret_key))
        from_address = wallet.public_key.to_base58check_address()
        txn = (
            tron.trx.transfer(from_address, to_address, amount)
            .memo("sending TRX")
            .build()
            .inspect()
            .sign(wallet)
            .broadcast()
        )

        txn.wait()

        print(txn)
    except Exception as e:
        exit(f"Submit failed: {e}")
