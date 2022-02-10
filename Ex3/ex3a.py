from sys import exit
from bitcoin.core.script import *

from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import send_from_P2PKH_transaction


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 3
##把x和y加起来，用OP_ADD脚本，它在执行的时候会把x和ypop掉然后再把结果push进栈里,接着拿这个result和原方程里的值比较是否一致
##加锁脚本实现了相加然后对比，和相减然后对比
ex3a_txout_scriptPubKey = [OP_2DUP,
OP_ADD,
192,
OP_EQUALVERIFY,
OP_SUB,
1220,
OP_EQUAL
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.001
    txid_to_spend = (
        'e8da1fdc9ac1500380614a1d561888ed6ba19c5764b582e9202aa131c9340a52')
    utxo_index = 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        ex3a_txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)
