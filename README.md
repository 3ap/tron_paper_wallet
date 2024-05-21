# TRON Paper wallet and beyond
Code for creating TRON paper wallet, getting the public address and sending TRX or USDT via TRON network to another TRON address

### Install the dependencies
```bash
pip3 install -r requirements.txt
```

### Run the create_wallet.py 
**to generate new wallet** and save secret key to file `secret_key.txt`
```bash
python3 create_wallet.py
```

### Run the get_public_address.py 
**to read public TRON address** to give it to the people who will send TRX or USDT to you in TRON network
```bash
python3 get_public_address.py
```

### Run the send_trx.py 
**to send TRX** to another TRON address
```bash
python3 send_trx.py
```

### Run the send_usdt.py 
**to send USDT** via TRON network to some TRON address
```bash
python3 send_usdt.py
```

## Learn more on the official TRON for developers web-site
Find comprehensive guides and documentation to help you start working with TRON as quickly as possible.

[TRON for developers](https://developers.tron.network)