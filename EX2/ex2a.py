from sys import exit
from bitcoin.core.script import *
from bitcoin.core.scripteval import _CheckMultiSig
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress

from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import send_from_P2PKH_transaction


cust1_private_key = CBitcoinSecret(
    'cU8Ra1PjNdL3q64dPBJssjRSD3db29tsHTBNRsoULsa9bZK2RGKS')
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret(
    'cS1rujJKTWDBoRbZC72RnKTaLpwfzLHEHk8L6fmAi5ruS7ypnBot')
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret(
    'cQtDN6FwxXr9m9ZssK4UkjVygcd67GqzJsgmFCuCRWcFVT3bcCcu')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.
ex2a_txout_scriptPubKey = [OP_DUP,OP_HASH160,my_address,OP_EQUALVERIFY,OP_CHECKSIGVERIFY,OP_1,cust1_public_key,cust2_public_key,cust3_public_key,OP_3,OP_CHECKMULTISIG]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.009
    txid_to_spend = (
        '1a048958dacb1425dac3114879a2700d7cf6c830166b416981e5fd07d3d51f83')
    utxo_index = 9
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        ex2a_txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)
