import sqlite3
import random
from datetime import datetime, timedelta

connect = sqlite3.connect('atm_app.db')
cursor = connect.cursor()




def create_account(name, phone_number, password):

    try:
        cursor.execute(f'''
            INSERT INTO users(name, phone_number, visa_number, cvv, exp_date, money, password) VALUES(?,?,?,?,?,?,?) 
                ''', (name, phone_number, random.randint(10**15, 10**16 - 1), random.randint(100, 999), (datetime.today() + timedelta(days=365*5)).strftime("%m/%y"), 0, password,))
    except:
        print("This informations are Used.")
        exit()


def show_info(number, password):

    cursor.execute("SELECT * FROM users WHERE visa_number = ?", (number,))

    info = cursor.fetchone()

    if info:
        if info[4] == password:

            print(f'''
                ---------YOUR INFO--------
                | Name: {info[1]}        
                | Phone: {info[2]}       
                | Visa number: {info[3]} 
                | Password: {info[4]}
                | CVV: {info[5]}         
                | Money: {info[7]}       
                | Expired date: {info[6]} 
                --------------------------        
            ''')
        else:
            print("Wrong password!")    
    else:
        print("Oops! this card isn't found.")    


def withdraw():

    print("-------------WITHDRAW------------")
    card_number = int(input("Enter your card number: \n"))
    passw = int(input("Enter your password: \n"))

    cursor.execute("SELECT money FROM users WHERE visa_number = ? AND password = ?", (card_number, passw,))

    money = cursor.fetchone() 

    if money:
        amount =  int(input("Type the amount you would like to withdraw: \n")) 

        if amount <= money[0]:
            new_money = money[0] - amount

            cursor.execute("UPDATE users SET money = ? WHERE visa_number = ?", (new_money, card_number,))
            print("Successful transaction!")

        else:
            print("Amount isn't enough.")
    else:
        print("Card number or Password is wrong!")        


def show_money(card_number, password):

    cursor.execute("SELECT money FROM users WHERE visa_number = ? AND password = ?", (card_number,password,))

    money = cursor.fetchone()

    if money:
        print(
            f'''
                -----YOUR MONEY-----
                | Money: {money[0]} |
                --------------------
            '''
        )
    else:
        print("Card number or Password is wrong!")


def deposite():
    print("-------------DEPOSITE------------")
    card_number = int(input("Enter your card number: \n"))
    passw = int(input("Enter your password: \n"))

    cursor.execute("SELECT money FROM users WHERE visa_number = ? AND password = ?", (card_number, passw,))

    money = cursor.fetchone()

    if money:
        amount =  int(input("Type the amount you would like to deposite: \n")) 

        new_money = money[0] + amount

        cursor.execute("UPDATE users SET money = ? WHERE visa_number = ?", (new_money, card_number,))

        print("Successful transaction!")

        show_money(card_number, passw)

    else:
        print("Card number or Password is wrong!")    



print("-----------------------------ATM-----------------------------------")
is_user = input("Do you have an account?(N/Y): \n")


if is_user.lower() == 'y':
    print('''
        Choose Proccess to do:
          [1] Withdraw.
          [2] Deposite.
          [3] Show my money.
          [4] Show my information.
    ''')

    print("-"*20)

    proccess = int(input("enter a number: "))

    if proccess == 1:
        withdraw()

    elif proccess == 2:
        deposite()

    elif proccess == 3:

        card_number = int(input("Enter your card number: \n"))
        password1 = int(input("Enter your password: \n"))
        show_money(card_number, password1)

    elif proccess == 4:

        print ('-'*20)
        number = input("Enter your card number: \n")
        password_input = int(input("Enter your password: \n"))
        show_info(number, password_input)

    else:
        print("Invalid choice")    

elif is_user.lower() == 'n':

    print('-'*20)
    create = input("Do you want to create new account?(Y/N): ")

    if create.lower() == "y":
        print('------Enter Your info------')
        name = input("Enter your name: ")
        phone_number = input("Enter your phone number: ")
        password = input("Enter a password for your card: ")
        print('---------------------------')

        create_account(name, phone_number, password)

        print("Account created successfully.")
        print("="*20)

        cursor.execute("SELECT visa_number, password FROM users WHERE name=?", (name,))

        info = cursor.fetchone()

        show_info(info[0], info[1])

    elif create.lower() == "n":
        print("You are welcome!")

    else:
        print("Invalid Choice.")


else:
    print("Invalid Choice.")



connect.commit()
cursor.close()
connect.close()