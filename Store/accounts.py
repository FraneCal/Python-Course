
import warehouse, it

accounts = {
        "001": {
            "User name": "admin",
            "Password": "admin123",
        },
        "002": {
            "User name": "warehouse",
            "Password": "warehouse123",
        },
        "003": {
            "User name": "sales",
            "Password": "sales123",
        },
        "004": {
            "User name": "buyer",
            "Password": "buyer123",
        },
        "005": {
            "User name": "administration",
            "Password": "administration123",
        },
    }


def users():
    while True:
        user_name = input('User name: ')
        password = input('Password: ')

        for account_id, account_info in accounts.items():
            if user_name == account_info['User name'] and password == account_info['Password']:
                if account_id == '001':
                    it.user_choice()
                elif account_id == '002':
                    warehouse.user_choice()
                elif account_id == '003':
                    pass
                elif account_id == '004':
                    pass
                elif account_id == '005':
                    pass
                return

        print('Incorrect username or password. Try again.')


def all_accounts():
    header = ["Product ID", "User name", "Password"]
    print("{:<15} {:<20} {:<15}".format(*header))
    print("-" * 55)

    for account_id, account_info in accounts.items():
        print("{:<15} {:<20} {:<15}".format(
            account_id,
            account_info["User name"],
            account_info["Password"],
        ))
    print()
    print()


def add_an_account():
    next_ID = str(f'00{len(accounts) + 1}')
    account_name = input('Enter a new user name: ')
    account_password = input('Enter a new password: ')
    accounts.update({
        next_ID: {
            "User name": f'{account_name}',
            "Password": f'{account_password}',
        }
    })
    print('Product added successfully.')

    all_accounts()


def delete_an_account():
    account_id = input("Enter the account ID you want to delete: ")

    if account_id in accounts:
        del accounts[account_id]
        print(f"Account with ID {account_id} has been deleted.")
    else:
        print(f"Account with ID {account_id} does not exist.")

    all_accounts()
