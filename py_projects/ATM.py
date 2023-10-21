import os
import time
import sqlite3
# make connection and set the curser and make the table
db = sqlite3.connect("ATM.db")
cr = db.cursor()
cr.execute("CREATE TABLE IF NOT EXISTS users(User_id integer, Name text, Address text, Age integer, Passw integer, Email text)")
# save the changes in database
def save_info() -> None:
    db.commit()
    db.close()
# clear the data on terminal
def clear() -> None:
    os.system("cls")
# show the welcome message to user
welcome_message = """Hello my dear client this is a simple ATM application you can use is easily:
    1- Create a new account.
    2- Login into your account.
    3- Exit."""
print(welcome_message)
# create a func to create a new account
class Account:
    num_user = 0
    @classmethod
    def new_account(cls):
        clear()
        cls.name = input("What is your name? ").strip().capitalize()
        while cls.name == "":
            print("please enter the name.")
            cls.name = input("What is your name? ").strip().capitalize()
        cls.address = input("What is your address? ").strip().capitalize()
        cls.age = int(input("What is your age? ").strip())
        while cls.age < 18:
            print("you are under the age, please make sure you are adult.")
            break
        else:
            cls.email = input("Enter the email: ").strip()
            while cls.email == "":
                print("please enter the email.")
                cls.email = input("What is your name? ").strip().capitalize()
            cls.passw = input("Enter the password: ").strip()
            while cls.passw == "":
                print("please enter the name.")
                cls.passw = input("Enter the password: ").strip().lower()
            cls.conf_pass  = input("Enter the confirm password: ").strip().lower()
            while cls.conf_pass != cls.passw:
                print("please enter the same password.")
                cls.conf_pass = input("Enter the confirm password: ").strip().lower()
            else:
                Account.num_user += 1
                cls.details = (Account.num_user, cls.name, cls.address, cls.age, cls.passw, cls.email)
                cr.execute("INSERT INTO users values(?,?,?,?,?,?)", cls.details)
                cr.execute("select user_id from users")
                Account.num_user = cr.fetchall()
                Account.num_user = Account.num_user[-1][0]
                Account.num_user += 1
                save_info()
                print("loading ......")
                time.sleep(1)
                print("Email is created.")
                time.sleep(0.3)
                clear()
try:
    user_input = int(input("Enter your option: ").strip())
    def start_the_program(option) -> int:
        if option == 1:
            Account.new_account()
        elif option == 2:
            pass
        elif option == 3:
            return 3
        options = [1, 2, 3]
        while option not in options:
            print("please enter the right option.")
            user_input = int(input("Enter your option: ").strip())
            start_the_program(user_input)
            break
except ValueError:
    print("only allowed integer.")
    user_input = int(input("Enter your option: ").strip())
start_the_program(user_input)
