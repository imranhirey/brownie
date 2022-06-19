from brownie import accounts,Simplestorage,config
import os
from dotenv import load_dotenv
def deploy_simple_storage():
    load_dotenv()
    print('infura id ',os.getenv("PRIVATE_KEY"))
    print('waaaw',config['wallets']['fromkey'])
    account= accounts.add(config['wallets']['fromkey'])
    simple_storage=Simplestorage.deploy({'from':account})
    print(simple_storage)
    stored_value=simple_storage.get()
    print('first value',stored_value)
    transaction=simple_storage.badalimran(76,{'from':account})
    transaction.wait(1)
    stored_value=simple_storage.get()
    print('updated value',stored_value)
   
    

def main():
    deploy_simple_storage()
   