
import products

options = ['1. State of the warehouse', '2. State for a certain product', '3. Add a product',
           '4. Change the state', '5. Logout']


def menu_options():
    print("-" * 35)
    print('\t\tWarehouse options:')
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
                products.all_products()
                menu_options()
            elif user_input == '2':
                products.single_product()
                menu_options()
            elif user_input == '3':
                products.add_a_product()
                menu_options()
            elif user_input == '4':
                products.change_the_state()
                menu_options()
            elif user_input == '5':
                print('See you next time.')
                should_continue = False
        except ValueError:
            print('Wrong input. Try again.')

