from brownie import Simplestorage,accounts
def test_deploy():
    account= accounts.load('imran')
    simple_storage=Simplestorage.deploy({'from':account})
    starting_value=simple_storage.get()
    expected_value=90
    assert starting_value==expected_value
def test_update():
    account= accounts.load('imran')
    simple_storage=Simplestorage.deploy({'from':account})
    expected=89
    simple_storage.badalimran(expected,{'from':account})
    actual=simple_storage.get()
    assert actual==expected
