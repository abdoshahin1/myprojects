from time import sleep
import os
import sys
import sqlite3

# clear the screen on terminal
def clear() -> None:
    os.system("cls")
# create database and set up the cursor and commit the changes
db = sqlite3.connect("ATM.db")
cr = db.cursor()
cr.execute("create table if not exists users (User_id integer, Name text, Address text, Age integer, Email text, Password text)")

welcome_message = """Hello my dear client this is a simple ATM application you can use:
    1- Create a new account.
    2- Login into your account.
    3- Exit."""
class Account:
    num_user = 1
    @classmethod
    def new_account(cls) -> None:
        sleep(1)
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
                db.commit()
                print("Loading........")
                sleep(1.5)
                print("Account is created.")
                sleep(1)
                clear()
            else:
                cr.execute("insert into users values(?,?,?,?,?,?)", details)
                db.commit()
                print("Loading........")
                sleep(2)
                print("Account is created.")
                sleep(1)
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
        if confirm_email in list_details and confirm_password in list_details:
            print("loading..........")
            sleep(1)
        else:
            print("You entered something wrong, please check the email or password then enter the correct details.")
            sleep(2)
            Account.logging()
    @classmethod
    def details(cls) -> None:
        clear()
        money = 0
        list_message = """ -------------------menu-------------------
            1 => Menu
            2 => Change password
            3 => Withdraw
            4 => Deposit
            5 => Money transfer
            6 => Total money
            7 => Exit
Enter the option: """
        cr.execute("select Password from users")
        password = cr.fetchall()
        try:
            option = int(input(list_message).strip())
        except ValueError:
            clear()
            print('enter the number only'.capitalize())
            sleep(2)
            Account.details()
        if option == 1:
            Account.details()
        elif option == 2:
            pass_change = input("Enter old password:").strip()
            for i in range(len(password)):
                if pass_change in password[i] : 
                    pass_change = input("Enter new password: ").strip()
                    confirm_pass_change = input("Confirm password: ").strip()
                    if confirm_pass_change == pass_change:
                        pass
                        #cr.execute(f"update users set Password = '{pass_change}' where Email = '{}'")
                    else:
                        print("check your password.")
                        Account.details()
                else:
                    print("please check your password.")
                    Account.details()
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            pass
        elif option == 6:
            print(f"your money is {money}$.")
        elif option == 7:
            start()
        else:
            print("please enter the correct option.")
            sleep(2)
            Account.details()
# start the program
def start():
        clear()
        print(welcome_message)
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
                    exit()
        except ValueError:
            clear()
            print("Only number allowed, Please enter option again.")
            sleep(1)
            start()
start()
db.close()