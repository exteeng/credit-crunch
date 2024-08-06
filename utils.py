import json 
from pathlib import Path

# data is dictionary 
# 10 keys
# keys: amount, date, location

def get_file(path: str) -> dict:

    path_file = Path(path)

    if path_file.exists():
        with path_file.open() as transactions_file:
            transactions = json.load(transactions_file)

    return transactions

transactions = get_file('data/transactions.json')
keys = list(transactions.keys())

# takes each account & reorganizes it
def get_account_info(account: dict) -> dict:
    amounts = []
    dates = []
    locations = []
    for item in account:
        amounts += [item['amount']]
        dates += [item['date']]
        locations += [item['location']]

    account_info = {'amounts': amounts, 'dates': dates, 'locations': locations}

    return account_info

def organize_accounts(transactions: dict) -> dict:
    account_summary = {}

    account_numbers = list(transactions.keys())

    for number in account_numbers:
        account = transactions[number]
        account_info = get_account_info(account)
        account_info['summed ammounts'] = sum(account_info['amounts'])
        account_summary[number] = account_info
    
    return account_summary

test_dict = organize_accounts(transactions)



# print(test_dict[keys[0]].keys())
# print(test_dict[keys[0]]['summed ammounts'])
# print(test_dict['8933640668918799'])

# python -m venv .venv
# source .venv/bin/activate
# pip install jupyterlab matplotlib


# OLD CODE

# def get_account_amounts(account: dict) -> list:
#     amounts = []
#     for item in account:
#         amounts += [item['amount']]

#     return amounts

# def get_all_amounts(transactions: dict) -> dict:

#     account_summary = {}

#     account_numbers = list(transactions.keys())
#     for number in account_numbers:
#         account = transactions[number]
#         account_amount = get_account_amounts(account)
#         account_summary[number] = account_amount
    
#     return account_summary

# test_dict = get_all_amounts(transactions)


# print(test_dict['8933640668918799'])
























