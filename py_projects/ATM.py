import os
import time
import sqlite3

# create database and set up the cursor and commit the changes
db = sqlite3.connect("ATM.db")
cr = db.cursor()
cr.execute("create table if not exists users (User_id integer, Name text, Address text, Age integer, Email text, Password text)")
def save_info() -> None:
    db.commit()
    db.close()
class Account:
    num_user = 1
    @classmethod
    def new_account(cls) -> None:
        name = input("enter your name: ").strip().capitalize()
        address = input("enter your address: ").strip().capitalize()
        while name == "" or address == "":
            print("please enter the priviest field.")
            name = input("enter your name: ").strip().capitalize()
            address = input("enter your address: ").strip().capitalize()
        age = int(input("enter your age: ").strip())
        if age < 18:
            print("you are underage, you do not pass the allowed limit for age.")
        else:
            email = input("enter your email: ").strip().capitalize()
            password = input("enter the password: ").strip()
            confirm_pass = input("confirm the pass: ").strip()
            while confirm_pass != password:
                print("please enter same password.")
                confirm_pass = input("confirm the pass: ").strip()
        details = (Account.num_user, name, address, age, email, password)
        cr.execute("insert into users values(?,?,?,?,?,?)", details)
        
