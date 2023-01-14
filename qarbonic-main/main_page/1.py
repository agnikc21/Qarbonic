import json
from py_algorand_sdk import account, algod, transaction

# Instantiate an algod client
algod_token = "YOUR_TOKEN_HERE"
algod_address = "https://testnet-algorand.api.purestake.io/ps2"
algod_client = algod.AlgodClient(algod_token, algod_address)

# Define the token parameters
token_id = "CCT"
amount = 10

# Define the sender and recipient address
sender_address = "SENDER_ADDRESS_HERE"
recipient_address = "RECIPIENT_ADDRESS_HERE"

# Get the account information for the sender address
sender_info = algod_client.account_info(sender_address)

# Check if the sender address has enough balance to complete the transaction
if sender_info["amount"] < amount:
    raise Exception("Not enough balance in the sender address")

# Create a transaction builder
txn = transaction.TransactionBuilder(sender_info["address"])

# Add the token transfer action
txn.add_token_transfer(sender_address, recipient_address, token_id, amount)

# Sign the transaction
txn.sign(sender_address)

# Send the transaction to the network
response = algod_client.send_transaction(txn)

# Print the response
print(json.dumps(response, indent=4))
