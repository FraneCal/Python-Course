import sqlite3
import re


class Database:

    def __init__(self):
        # Creating the database, connect to it, and create a cursor
        create_table_query = '''CREATE TABLE IF NOT EXISTS Employees (
                        id INTEGER PRIMARY KEY,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE,
                        department TEXT NOT NULL
                        );
    '''
        database_name = 'Tvrtka.db'

        self.sc = sqlite3.connect(database_name)
        self.cursor = self.sc.cursor()
        self.cursor.execute(create_table_query)

    def menu(self):
        while True:
            login_name = input('Enter your email: ')

            # Go through the database
            self.cursor.execute("SELECT email, department FROM Employees WHERE email=?", (login_name,))
            user_email = self.cursor.fetchone()

            if user_email:
                email, department = user_email

                # If the main admin is logging in, print out the following menu
                if email == 'admin@net.hr' and department == 'IT':
                    while True:
                        admin_menu = ['1. Add new user', '2. Show all users', '3. Delete a user',
                                      '4. Delete all users', '5. Change the department', '6. Exit']
                        print("Main IT department.")
                        print('**** MENU ****')
                        for info in admin_menu:
                            print(info)
                        user_input = input('\nChoose an action: ')
                        match user_input:
                            case '1':
                                self.add_user()
                            case '2':
                                self.show_all_users()
                            case '3':
                                self.delete_a_user()
                            case '4':
                                self.delete_all_users()
                            case '5':
                                self.change_the_department()
                            case '6':
                                print('See you next time.')
                                print()
                                break
                            case _:
                                print('Wrong input. Try again.')
                                print()

                # If he/she is in HR department print out the following menu
                elif department == 'HR':
                    print("HR department.")
                    while True:
                        hr_menu = ['1. Show all users', '2. Contact IT', '3. Exit']
                        print('**** MENU ****')
                        for info in hr_menu:
                            print(info)
                        user_input = input('\nChoose an action: ')
                        match user_input:
                            case '1':
                                print('In construction.')
                            case '2':
                                print('In construction.')
                            case '3':
                                print('See you next time.')
                                print()
                                break
                            case _:
                                print('Wrong input. Try again.')
                                print()

                # If he/she is in IT department print out the following menu
                elif department == 'IT':
                    print("IT department.")
                    while True:
                        hr_menu = ['1. Add a user', '2. Delete a user', '3. Exit']
                        print('**** MENU ****')
                        for info in hr_menu:
                            print(info)
                        user_input = input('\nChoose an action: ')
                        match user_input:
                            case '1':
                                print('In construction.')
                            case '2':
                                print('In construction.')
                            case '3':
                                print('See you next time.')
                                print()
                                break
                            case _:
                                print('Wrong input. Try again.')
                                print()

            # Empty field to exit the program
            elif login_name == '':
                print()
                self.cursor.close()
                self.sc.close()
                print('See you next time.')
                break

            # If anything else is inputted print out the following error message
            else:
                print()
                print('Wrong input. Try again.')
                print()

    def add_user(self):
        users = []
        while True:
            # Asking for new user info
            first_name = input('Enter first name: ').title()

            if first_name == '':
                print("User name can't be empty. Please try again.")

            last_name = input('Enter last name: ').title()
            if last_name == '':
                print("User name can't be empty. Please try again.")

            user_email = input('Enter user email: ')
            if not re.match(r"[^@]+@[^@]+\.[^@]+", user_email):
                print("Wrong format. Please try again.")

            department = input('Enter department (IT, HR): ').upper()
            if department != 'IT' or department != 'HR':
                print('That department does not exist.')

            # Append it to the empty list in a tuple
            users.append((first_name, last_name, user_email, department))
            break

        # If everything is okay, add the user
        self.cursor.executemany('INSERT INTO Employees(first_name, last_name, email, department) VALUES (?,?,?,?)', users)
        self.sc.commit()
        print()
        print('User successfully added.')
        print()

    def show_all_users(self):
        print()

        # Fetch all the users from the database
        rows = self.cursor.execute('SELECT * FROM Employees').fetchall()

        # If there aren't any users in the database print out the following
        if not rows:
            print('There are no users in the database.')

        # If there are users, print them out one by one
        else:
            for row in rows:
                '''
                The star is here to remove the brackets, if you print it out without a star it will
                print it out as a tuple
                '''
                print(*row)
        print()

    def delete_all_users(self):
        self.cursor.execute('DELETE FROM Employees')
        while True:
            user_input = input("Are you sure you want to delete all users (y/n), (or 'q' for back): ")

            if user_input == 'q':
                print()
                return

            if user_input == 'y':
                self.sc.commit()
                break
            elif user_input == 'n':
                return
            else:
                print('Wrong input.')
        print()
        print('All users are deleted.')
        print()

    def delete_a_user(self):
        delete_query = '''
        DELETE FROM Employees WHERE email = ?
        '''
        while True:
            user_email = input("Enter the email of the user that you want to delete (or 'q' for back): ")

            if user_email == 'q':
                print()
                return

            # Checking if the user has entered the right email format
            if not re.match(r"[^@]+@[^@]+\.[^@]+", user_email):
                print("Wrong format. Please try again.")
                continue

            try:
                self.cursor.execute(delete_query, (user_email,))
                rows_affected = self.cursor.rowcount
                self.sc.commit()
                # If the user has entered the right email format, but that user doesn't exist print out the following
                if rows_affected == 0:
                    print("User does not exist.")
                    continue
                # If the right email format has been entered, and the user exist, delete him
                else:
                    print()
                    print("User deleted successfully.")
                print()
                break
            except Exception as e:
                print(f"An error occurred: {e}")

    def change_the_department(self):
        while True:
            user_email = input("Enter the email of the user you want to change the department for (or 'q' for back): ")

            if user_email == 'q':
                print()
                return

            try:
                self.cursor.execute('SELECT * FROM Employees WHERE email = ?', (user_email,))
                user = self.cursor.fetchone()

                # Checking if the user exists (no matter the email format)
                if user is None:
                    print("User does not exist.")
                    continue

                # If the user exists, check if that department exists
                while True:
                    new_department = input('Enter the new department: ').upper()
                    if new_department != 'IT' and new_department != 'HR':
                        print('That department does not exist.')
                        continue

                    # If the user exists, and the department exists, update the users department
                    self.cursor.execute('UPDATE Employees SET department = ? WHERE email = ?',
                                        (new_department, user_email))
                    self.sc.commit()
                    print()
                    print('Department changed successfully.')
                    print()
                    break

                break
            except Exception as e:
                print(f"An error occurred: {e}")
