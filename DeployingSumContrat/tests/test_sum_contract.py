from brownie import accounts, SumContract


def test_deploy():
    # testing if the value initialize with the deployment of the contract is equal to 0
    # msg.sender account
    account = accounts[1]

    sum_contract = SumContract.deploy({"from": account})
    

    # calling view function
    initial_value = sum_contract.retrive()
    expected = 0

    assert expected == initial_value

    # terminal command:
    # brownie test
    # brownie test - k(specific function)
    # brownie test --pdb (more specific/ useful when i'm debbuging) -- break -- import os; os._exit(0)


def test_sum_function():
    account = accounts[1]
    sum_contract = SumContract.deploy({"from": account})
    # calling function
    transaction = sum_contract.Sum(65, 56, {"from": account})
    expected = 121
    assert expected == sum_contract.retrive()
