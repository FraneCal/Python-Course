#NOT FINISHED

#Gym membership cards: see users, add users, delete, users

members = {
        '1': {
            'First name:': 'John',
            'Last name': 'Andrew',
            'Member from': 2020,
            'Valid until': 2024,
            'Type': 'Basic'
        },
        '2': {
            'First name:': 'Peter',
            'Last name': 'Johnson',
            'Member from': 1995,
            'Valid until': 2030,
            'Type': 'Premium'
        }
    }


def check_if_a_member_exists(members):
    f_name = input('Enter first name: ')
    l_name = input('Enter last name: ')

    for key, value in members.items():
        for nested_key, nested_value in value.items():
            #Check if there is a user with the given first name
            if nested_key == 'First name:' and nested_value == f_name:
                # If there is then check if there is a user with the given last name
                if value.get('Last name') == l_name:
                    print(f'The member "{f_name} {l_name}" was found.')
                    return
    else:
        print(f'The member "{f_name} {l_name}" was not found.')

    


def show_a_member(members):
    show_a_member = input('Which member do you want to see: ')
    for key, value in members.items():
        if key == show_a_member:
            print(value)


def show_all_members(members):
    #Printing out all the members to see if everything is okey
    for key, value in members.items():
        print(key, value)


def new_member(members):
    # Get the next available ID
    next_ID = str(len(members) + 1)
    # Info about the new member
    f_name = input('Enter the first name: ')
    l_name = input('Enter the last name: ')
    member_from = input('Beginning of the membership: ')
    valid_until = input('Membership valid until: ')
    type_of_membership = input('Type of membership, Basic or Premium: ')
    members.update({
        next_ID: {
            'First name:': f'{f_name}',
            'Last name': f'{l_name}',
            'Member from': f'{member_from}',
            'Valid until': f'{valid_until}',
            'Type': f'{type_of_membership}'
        }
    })
    #Printing out all the members to see if everything is okey
    for key, value in members.items():
        print(key, value)


def delete_a_member(members):
    delete_a_user = input('Which member do you want to delete (e.g. 2: ')
    #Deleting a user
    del members [delete_a_user]
    #Printing out all the members to see if everything is okey
    for key, value in members.items():
        print(key, value)


def handle_choice(members, user_choice):
    if user_choice == '1':
        check_if_a_member_exists(members)
        show_a_member(members)
    elif user_choice == '2':
        show_all_members(members)
    elif user_choice == '3':
        new_member(members)
    else:
        check_if_a_member_exists(members)
        delete_a_member(members)



user_choice = ''
while user_choice != 'Quit':
    user_choice = input(
        '\nWelcome to the members club. Here are the following options: \n1. Show a specific member\n2. Show all members\n3. Add members\n4. Delete members\n\nWhich action do you want choose:').title()

    handle_choice(members, user_choice)
