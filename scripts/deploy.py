from brownie import accounts, config, SumContract, network

# accounts availible, browniecofig.yaml, my contract


def deploySumContract():
    account = accounts[0]
    print(account)
    sum_contract = SumContract.deploy({"from": account})

    # calling sum  function
    transaction = sum_contract.Sum(15, 9, {"from": account})
    transaction.wait(1)

    # calling view function, which don't need to strat a transaction
    value_sum = sum_contract.retrive()
    print("Transaction 1", value_sum)

    # calling sum  function
    transaction = sum_contract.Sum(15, 9, {"from": account})
    transaction.wait(1)

    value_sum = sum_contract.retrive()
    print("Transaction 2", value_sum)

    print()


def main():
    deploySumContract()
