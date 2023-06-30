import sqlite3, re

class Database:

  def __init__(self):
    create_table_query = '''CREATE TABLE IF NOT EXISTS Employees (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE
                        );
    '''
    database_name = 'Tvrtka.db'

    self.sc = sqlite3.connect(database_name)
    self.cursor = self.sc.cursor()
    self.cursor.execute(create_table_query)

  
  def menu(self):
    while True:
      menu = ['1. Add new user', '2. Show all users', '3. Delete all users', '4. Exit']
      print('**** MENU ****')
      for info in menu:
        print(info)
      user_input = input('\nChoose an action: ')
      match user_input:
        case '1':
          self.add_user()
        case '2':
          self.show_all_users()
        case '3':
          self.delete_all_users()
        case '4':
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
    users.append((user_name, user_email))

    self.cursor.executemany('INSERT INTO Employees(name, email) VALUES (?,?)', users)
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
    self.sc.commit()
    print()
    print('All users are deleted.')
    print()
