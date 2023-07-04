import sqlite3, re

class Database:

  def __init__(self):
    create_table_query = '''CREATE TABLE IF NOT EXISTS Employees (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        pass INT NOT NULL,
                        email TEXT NOT NULL UNIQUE,
                        department TEXT NOT NULL
                        );
    '''
    database_name = 'Lista_osoba.db'

    self.sc = sqlite3.connect(database_name)
    self.cursor = self.sc.cursor()
    self.cursor.execute(create_table_query)

  
  def login(self):
    print('**** LOGIN ****')
    print()
    user_name=input("Inesrt user name:\n\n")
    print()
    user_pass=input("Insert password:\n\n")
    print()
    return user_name, user_pass
  
  def menu_admin(self):
      while True:
        menu = ['1. Add new user', '2. Show all users', '3. Delete all users', '4. Delete user', '5. Filter users by department', '5. Exit']
        print('**** MENU ****')
        for info in menu:
          print(info)
          print()
        user_input = input('\nChoose an action: ')
        match user_input:
          case '1':
            self.add_user()
          case '2':
            self.show_all_users()
          case '3':
            self.delete_all_users()
          case '4':
            self.show_all_users()
            user_id=input('Enter the ID of the user to delete: ')
            self.delete_user_by_id(user_id)
          case '5':
            department = input('Enter the department to filter users (HR, IT, SALES): ').upper()
            self.show_users_by_department(department)
          case '6':
            print('See you next time.')
            if self.sc:
              self.cursor.close()
              self.sc.close()
            break
          case _:
            print('Wrong input. Try again.')
            print()

  
  def add_user(self):
    users = []
    while True:
      user_name = input('Enter user name: ')
      if user_name:
        break
      else:
        print("User name can't be empty. Please try again.")
    while True:
      user_email = input('Enter user email: ')
      if re.match(r"[^@]+@[^@]+\.[^@]+", user_email):
        break
      else:
        print("Wrong format. Please try again.")
    while True:
      user_pass = input('Enter user password: ')
      if user_pass:
        break
      else:
        print("User password can't be empty. Please try again")
    while True:
      user_department_list=['HR', 'IT','SALES']
      user_department=input('Enter the relevant user department (HR,IT,SALES): ').upper()
      if user_department not in user_department_list:
        print('Department not exist')
      else:
        break
      
    users.append((user_name, user_email, user_pass, user_department))

    self.cursor.executemany('INSERT INTO Employees(name, email, pass, department) VALUES (?,?,?,?)', users)
    self.sc.commit()
    print()
    print('User successfully added.')
    print()
    return users
  
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
    self.sc.commit()
    print()
    print('All users are deleted.')
    print()

  def delete_user_by_id(self, user_id):
    self.cursor.execute('DELETE FROM Employees WHERE id = ?', (user_id,))
    self.sc.commit()
    print()
    print('User with ID', user_id, 'is deleted.')
    print()

  def menu(self):
    pass

  def show_users_by_department(self, department):
        print()
        rows = self.cursor.execute('SELECT Id, NAME FROM Employees WHERE department = ?', (department,)).fetchall()
        if not rows:
            print(f'There are no users in the database with department: {department}')
        else:
            print(f'Users in department {department}:')
            for row in rows:
                print(*row)
        print()
