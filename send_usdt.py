from tronpy import Tron, keys
from tronpy.providers import HTTPProvider

def usdt_to_sun(usdt_amount):
    return int(usdt_amount * 1000000)

api_key="03f17615-a928-4406-bc14-ad61373427ef" # Get it from https://www.trongrid.io/dashboard
to_address = "TNuTtmTdmdGWKQSnySroeXjyzGh1ZsRau2" # Where you want to send your USDT
amount = usdt_to_sun(1.18)  # The amount of USDT to send

secret_key = ''
with open("secret_key.txt", "r") as secret_key_file:
    secret_key = secret_key_file.read().strip()
    
tron = Tron(HTTPProvider(api_key=api_key))

contract_address = 'TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t' # USDT token on mainnet

abi = [{
     "outputs":[
        {
           "type":"bool"
        }
     ],
     "inputs":[
        {
           "name":"_to",
           "type":"address"
        },
        {
           "name":"_value",
           "type":"uint256"
        }
     ],
     "name":"transfer",
     "stateMutability":"Nonpayable",
     "type":"Function"
  }]

contract = tron.get_contract(contract_address)
contract.abi = abi

if secret_key:
    try:
        wallet = keys.PrivateKey(bytes.fromhex(secret_key))
        from_address = wallet.public_key.to_base58check_address()
        txn = (
            contract.functions.transfer(to_address, amount)
            .with_owner(from_address)
            .fee_limit(50_000_000)
            .build()
            .inspect()
            .sign(wallet)
            .broadcast()
        )

        txn.wait()

        print(txn)
    except Exception as e:
        exit(f"Submit failed: {e}")
