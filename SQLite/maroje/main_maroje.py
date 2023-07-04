from database_class_maroje import Database

database = Database()

while True:
    user_name, user_pass = database.login()
    if user_name == "Admin" and user_pass == "1234":
        database.menu_admin()
    else:
        database.menu()