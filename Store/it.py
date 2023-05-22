
import accounts, main

options = ['1. All accounts', '2. Add an account',
           '3. Delete an account', '4. Logout']


def menu_options():
    print("-" * 35)
    print('\t\tIT options:')
    print("-" * 35)
    for option in options:
        print(option)
    print()


def user_choice():
    menu_options()
    should_continue = True
    while should_continue:
        try:
            user_input = input('Choose an option: ')
            if user_input == '1':
                accounts.all_accounts()
                menu_options()
            elif user_input == '2':
                accounts.add_an_account()
                menu_options()
            elif user_input == '3':
                accounts.delete_an_account()
                menu_options()
            elif user_input == '4':
                print('See you next time.')
                print()
                should_continue = False
        except ValueError:
            print('Wrong input. Try again.')
    main.main()


user_choice()
