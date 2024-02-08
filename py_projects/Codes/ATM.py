import os
import re
import sys
import sqlite3
from time import sleep

# clear the screen on terminal
def clear() -> None:
    os.system("cls")
# create database and set up the cursor and commit the changes
db = sqlite3.connect("ATM.db")
cr = db.cursor()
cr.execute("create table if not exists users (User_id integer, Name text, Address text, Age integer, Email text, Password text, Money integer)")
class Account:
    user_pass= 0
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
            vialed_email = re.findall(r"[A-z0-9\_?]+@\w{5}\.com", email)
            while vialed_email == []: 
                print("please, enter your gmail correctly.")
                email = input("Enter your email: ").strip().capitalize()
                vialed_email = re.findall(r"[A-z0-9\_?]+@\w{5}\.com", email)
            else:
                password = input("Enter the password: ").strip()
                confirm_pass = input("Confirm the pass: ").strip()
            while confirm_pass != password:
                print("Please enter same password.")
                confirm_pass = input("Confirm the pass: ").strip()
            try:
                money = int(input("Enter Money: ").strip())
                print("done added money.")
            except ValueError:
                print("please, enter number only.")
                money = int(input("Enter Money: ").strip())
                print("done added money.")
            details = (Account.num_user, name, address, age, email, password, money)
            cr.execute("select * from users")
            all_data = cr.fetchall()
            if all_data != []:
                cr.execute("insert into users values(?,?,?,?,?,?,?)", details)
                Account.num_user = all_data[-1][0] + 1
                cr.execute(f"update users set User_id = {Account.num_user} where Name = '{name}' ")
                db.commit()
                print("Loading........")
                sleep(1.5)
                print("Account is created.")
                sleep(1)
                clear()
            else:
                cr.execute("insert into users values(?,?,?,?,?,?,?)", details)
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
        confirm_password = input("Enter the password: ").strip()
        for num in range(len(data)):
            list_details.append(data[num][0])
            list_details.append(data[num][1])
        if confirm_email in list_details and confirm_password in list_details:
            Account.user_pass = confirm_password 
            print("loading..........")
            sleep(0.6)
            clear()
        else:
            print("You entered something wrong, please check the email or password then enter the correct details.")
            sleep(2)
            Account.logging()
    @classmethod
    def details(cls) -> None:
        cr.execute("select * from users")
        details = cr.fetchall()
        for M in range(len(details)):
            if Account.user_pass in details[M]:
                all_info = details[M]
                new_money = details[M][-1]
        list_message = """ -----------------Menu-----------------
            1 => Menu
            2 => Display info
            3 => Change password
            4 => Deposit
            5 => Withdraw 
            6 => Money transfer
            7 => Total money
            8 => Exit
Enter the option: """ 
        try:
            option = int(input(list_message).strip())
        except ValueError:
            print('enter the number only'.capitalize())
            sleep(2)
            Account.details()
        if option == 1:
            clear()
            Account.details()
        elif option == 2:
            for info in range(len(all_info)):
                clear()
                print(f"""-----------------My Information-----------------
                    Name => {all_info[1]}
                    Address => {all_info[2]}
                    Age => {all_info[3]}
                    Email => {all_info[4]}
                    Password => {all_info[5]}
                    Money => {all_info[6]}""")
                break
            Account.details()
        elif option == 3:
            clear()
            pass_change = input("Enter old password:").strip()
            if pass_change == Account.user_pass : 
                pass_change = input("Enter new password: ").strip()
                confirm_pass_change = input("Confirm password: ").strip()
                if confirm_pass_change == pass_change:
                    cr.execute(f"update users set Password = '{pass_change}' where Password = '{Account.user_pass}'")
                else:
                    print("please, enter the same password.")
                    confirm_pass_change = input("Confirm password: ").strip()
                    if confirm_pass_change == pass_change:
                        cr.execute(f"update users set Password = '{pass_change}' where Password = '{Account.user_pass}'")
            db.commit()
            print("Your password is updated.")
            Account.details()
        elif option == 4:
            input_money = int(input("Enter your money: ").strip())
            cr.execute(f"update users set Money = {new_money + input_money} where Password = '{Account.user_pass}'")
            db.commit()
            print("money is deposited")
            sleep(0.9)
            Account.details()
        elif option == 5:
            try:
                input_money = int(input("Enter your money: ").strip())
                if input_money < new_money:
                    cr.execute(f"update users set Money = {new_money - input_money} where Password = '{Account.user_pass}'")
                    print("money is withdraw")
                    db.commit()
                    sleep(0.9)
                    Account.details()
            except:
                print("""You have money less than that you entered.
                        please, enter money again.""")
                input_money = int(input("Enter your money: ").strip())
                if input_money < new_money:
                    cr.execute(f"update users set Money = {new_money - input_money} where Password = '{Account.user_pass}'")
                    print("money is withdraw")
                    db.commit()
                    sleep(0.9)
                    Account.details()
        elif option == 6:
            pass
        elif option == 7:
            print(f"your money is {new_money}$.")
            sleep(1)
            Account.details()
        elif option == 8:
            start()
        else:
            print("please enter the correct option.")
            sleep(2)
            Account.details()
# start the program
def start():
        clear()
        print("""Hello my dear client this is a simple ATM application you can use:
    1- Create a new account.
    2- Login into your account.
    3- Exit.""")
        try:
            option = int(input("Enter the option: ").strip())
            while option not in [1, 2, 3]:
                print("Please Enter the right option.")
                option = int(input("Enter the option: ").strip())
            if option == 1:
                Account.new_account()
                Account.details()
            elif option == 2:
                Account.logging()
                Account.details()
            else:
                exit()
        except ValueError:
            clear()
            print("Only number allowed, Please enter option again.")
            sleep(1)
            start()
start()
db.close()