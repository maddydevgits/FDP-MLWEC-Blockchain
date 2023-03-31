from web3 import Web3,HTTPProvider
import json

def connect_with_blockchain(acc):
    try:
        # Stage - 1: Connecting with RPC Server
        rpcServer='http://127.0.0.1:7545'
        web3=Web3(HTTPProvider(rpcServer))
        print('Connected with Blockchain')
        
        # Stage - 2: From which account you have to make transactions
        if acc=='0':
            web3.eth.defaultAccount=web3.eth.accounts[0]
        web3.eth.defaultAccount=acc

        # Stage - 3: to which contract you have to access
        artifact_path='../build/contracts/sms.json'
        with open(artifact_path) as f:
            contract_json=json.load(f)
            contract_abi=contract_json['abi']
            contract_address=contract_json['networks']['5777']['address']
        
        # Stage - 4: Using Contract ABI, Contract Address
        contract=web3.eth.contract(address=contract_address,abi=contract_abi)

        return contract,web3
    except:
        print('Error Connecting with Blockchain')

contract,web3=connect_with_blockchain('0xc55A47516fc953bcde3C4A6d08519A862B4aA0c4')
tx_hash=contract.functions.insertMessage('Hi FDP is going great').transact()
web3.eth.waitForTransactionReceipt(tx_hash)
print('Transaction Stored in a Block')


contract,web3=connect_with_blockchain('0xc55A47516fc953bcde3C4A6d08519A862B4aA0c4')
print(contract.functions.viewMessages().call()) # call is used to invoke view functions
