
import warehouse, sales, buyer, administration


def users():
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
    while True:
        try:
            user_name = input('User name: ')
            password = input('Password: ')
            if user_name == accounts['001']['User name'] and password == accounts['001']['Password']:
                pass
            elif user_name == accounts['002']['User name'] and password == accounts['002']['Password']:
                warehouse.user_choice()
            elif user_name == accounts['003']['User name'] and password == accounts['003']['Password']:
                pass
            elif user_name == accounts['004']['User name'] and password == accounts['004']['Password']:
                pass
            elif user_name == accounts['005']['User name'] and password == accounts['005']['Password']:
                pass
            return
        except ValueError:
            print('Wrong input. Try again.')

