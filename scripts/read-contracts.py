from brownie import accounts,Simplestorage,config


def readcontract():
    simplestorage= Simplestorage[-1]
    value=simplestorage.get()
    print('value',value)


def main():
    readcontract()
