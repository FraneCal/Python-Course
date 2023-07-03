import sqlite3
import re


class Database:

    def __init__(self):
        # Creating the database, connecting to it, and creating the cursor
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
            login_name = input('Enter your username: ')
            login_password = input('Enter your password: ')

            if login_name == 'admin' and login_password == 'admin123':
                while True:
                    admin_menu = ['1. Add new user', '2. Show all users', '3. Delete a user',
                                  '4. Delete all users', '5. Change the department', '6. Exit']
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
                            if self.sc:
                                self.cursor.close()
                                self.sc.close()
                            break
                        case _:
                            print('Wrong input. Try again.')
                            print()

            elif login_name == 'hr' and login_password == 'hr123':
                while True:
                    hr_menu = ['1. Show all users', '2. Exit']
                    print('**** MENU ****')
                    for info in hr_menu:
                        print(info)
                    user_input = input('\nChoose an action: ')
                    match user_input:
                        case '1':
                            self.show_all_users()
                        case '2':
                            print('See you next time.')
                            if self.sc:
                                self.cursor.close()
                                self.sc.close()
                            break
                        case _:
                            print('Wrong input. Try again.')
                            print()

            elif login_name == '' and login_password == '':
                print()
                print('See you next time.')
                break

            else:
                print()
                print('Wrong input. Try again.')
                print()

    def add_user(self):
        users = []
        while True:
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

            users.append((first_name, last_name, user_email, department))
            break

        self.cursor.executemany('INSERT INTO Employees(first_name, last_name, email, department) VALUES (?,?,?,?)', users)
        self.sc.commit()
        print()
        print('User successfully added.')
        print()

    def show_all_users(self):
        print()
        rows = self.cursor.execute('SELECT * FROM Employees').fetchall()

        if not rows:
            print('There are no users in the database.')

        else:
            for row in rows:
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
                # If the user has entered the right email format, but that user doesn't exist
                if rows_affected == 0:
                    print("User does not exist.")
                    continue
                # If the right email format has beeen entered, and the user exist, delete him
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

