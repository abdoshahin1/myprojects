import os
import sys
from time import sleep
import sqlite3

# clear the screen on terminal
def clear() -> None:
    os.system("cls")
# create database and set up the cursor and commit the changes
db = sqlite3.connect("ATM.db")
cr = db.cursor()
cr.execute("create table if not exists users (User_id integer, Name text, Address text, Age integer, Email text, Password text)")
def save_info() -> None:
    db.commit()
    db.close()

welcome_message = """Hello my dear client this is a simple ATM application you can use is easily:
    1- Create a new account.
    2- Login into your account.
    3- Exit."""
print(welcome_message)
class Account:
    num_user = 1
    @classmethod
    def new_account(cls) -> None:
        sleep(0.7)
        clear()
        name = input("Enter your name: ").strip().capitalize()
        address = input("Enter your address: ").strip().capitalize()
        while name == "" or address == "":
            print("Please enter the priviest field.")
            name = input("Enter your name: ").strip().capitalize()
            address = input("Enter your address: ").strip().capitalize()
        age = int(input("Enter your age: ").strip())
        if age < 18:
            print("You are underage, you do not pass the allowed limit for age.")
        else:
            email = input("Enter your email: ").strip().capitalize()
            password = input("Enter the password: ").strip()
            confirm_pass = input("Confirm the pass: ").strip()
            while confirm_pass != password:
                print("Please enter same password.")
                confirm_pass = input("Confirm the pass: ").strip()
            details = (Account.num_user, name, address, age, email, password)
            cr.execute("select * from users")
            all_data = cr.fetchall()
            if all_data != []:
                cr.execute("insert into users values(?,?,?,?,?,?)", details)
                Account.num_user = all_data[-1][0] + 1
                cr.execute(f"update users set User_id = {Account.num_user} where Name = '{name}' ")
                save_info()
                print("Loading........")
                sleep(1.5)
                print("Account is created.")
                sleep(0.7)
                clear()
            else:
                cr.execute("insert into users values(?,?,?,?,?,?)", details)
                save_info()
                print("Loading........")
                sleep(1.5)
                print("Account is created.")
                sleep(0.7)
                clear()
    @classmethod
    def logging(cls) -> None:
        cr.execute("select Email, Password from users")
        data = cr.fetchall()
        clear()
        list_details = []
        confirm_email = input("Enter the email: ").strip().capitalize()
        confirm_password = input("Enter th password: ").strip()
        for num in range(len(data)):
            list_details.append(data[num][0])
            list_details.append(data[num][1])
        if confirm_email in list_details or list_details:
            print("loading..........")
            sleep(1)
        else:
            print("You entered something wrong, please check the email or password then enter the correct details.")
            Account.logging()
    @classmethod
    def details(cls) -> None:
        clear()
        list_message = """ -------------------menu-------------------
    1-menu
    2-Edit your email
    3-Edit your password
    4-withdraw
    5-deposit
    6-money transfer
    7-total money
    8-exit"""
        print(list_message.capitalize())
    @classmethod
    def start(cls):
        try:
            option = int(input("Enter the option: ").strip())
            while option not in [1, 2, 3]:
                print("Please Enter the right option.")
                option = int(input("Enter the option: ").strip())
            else:
                if option == 1:
                    Account.new_account()
                    Account.details()
                elif option == 2:
                    Account.logging()
                    Account.details()
                elif option == 3:
                    pass
        except ValueError:
            clear()
            print("Only number allowed, Please enter option again.")
            sleep(1)
            Account.start()
# start the program
Account.start()