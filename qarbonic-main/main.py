import json
import base64
import algosdk
from algosdk import account
from algosdk.v2client import algod
from algosdk import transaction
import time


def getting_started_example():

  algod_address = 'https://academy-algod.dev.aws.algodev.network/'
  algod_token = "2f3203f21e738a1de6110eba6984f9d03e5a95d7a577b34616854064cf2c0e7b"
  algod_client = algod.AlgodClient(algod_token, algod_address)

  secret_key, my_address = (
    'up2vXEgqa0B4NL3LY+TfVSaRPwxtdbN8yyRiP6xKmbNK/DXi4vYM5FcwJTWHATLivMyh7yisbeufWu/IQTxrzQ==',
    'JL6DLYXC6YGOIVZQEU2YOAJS4K6MZIPPFCWG3247LLX4QQJ4NPGTEBD6QQ')

  account_info = algod_client.account_info(my_address)

  m = int(account_info.get('amount'))
  x = int(input("Enter the no. of CCT you are buying: "))
  y = int(input("Enter the price you are willing to pay per CCT: "))
  print("Please send ", x * y, " ALGO here: {}".format(my_address))
  completed = input("Press 'Enter' once you have funded the account: ")

  if completed == "":
    account_info = algod_client.account_info(my_address)
    if account_info.get('amount') >= m + 10000 * x * y:
      index = 153874264

      print("Building transaction")
      params = algod_client.suggested_params()
      receiver = str(input("Enter your address to receive CCT Tokens: "))

      amount = int(100 * x)
      closeto = ""
      unsigned_txn = transaction.AssetTransferTxn(my_address, params, receiver,
                                                  amount, index, closeto)

      print("Signing transaction")
      signed_txn = unsigned_txn.sign(secret_key)
      print("Sending transaction")
      txid = algod_client.send_transaction(signed_txn)
      print('Transaction Info:')
      print("Signed transaction with txID: {}".format(txid))
    else:
      print("We have not received the funds!")
  else:
    print("Error")


getting_started_example()
