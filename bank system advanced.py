import os
import time
import string

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') # To Clear Screen 

Users = []

# ================== AUTH ==================
def authenticate(user): # Check The Name Of User And Tries 
    tries = 3
    while tries > 0:
        try:
            pin = int(input("Enter Your PIN : "))
        except ValueError:
            print("PIN must be numbers only")
            continue

        if pin == user["PIN"]:
            return True
        else:
            tries -= 1
            print(f"Wrong PIN, remaining tries: {tries}")

    print("❌ Wrong PIN 3 times")
    return False

# ================== CREATE ACCOUNT ==================

numbers = string.digits


def created_account():
    # ===== Name =====
    Name = input("Enter The Name : ").strip().lower()

    # name can't start with digit
    for num in numbers:
        if Name.startswith(num):
            print("Error: Name Cannot Start With A Digit")
            return

    # name can't contain spaces
    for ch in Name:
        if ch == " ":
            print("Error: Remove Spaces From Name")
            return

    # name must end with @account.com
    if not Name.endswith("@account.com"):
        print("Error: Name Must End With '@account.com'")
        return

    # ===== Numbers Input =====
    try:
        ID = int(input("Enter 3-Digits ID : "))
        PIN = int(input("Enter 6-Digits PIN : "))
        Balance = float(input("Enter Your Balance : "))
    except ValueError:
        print("Error: Numbers Only Allowed For ID, PIN And Balance")
        return

    # ===== ID & PIN Length (Detailed) =====
    if len(str(ID)) != 3 and len(str(PIN)) != 6:
        print("Error: ID Must Be 3 Digits AND PIN Must Be 6 Digits")
        return
    elif len(str(ID)) != 3:
        print("Error: ID Length Is Wrong (Must Be 3 Digits)")
        return
    elif len(str(PIN)) != 6:
        print("Error: PIN Length Is Wrong (Must Be 6 Digits)")
        return

    # ===== Duplicate Account Check =====
    for user in Users:
        if user["Name"] == Name:
            print("Error: This Account Already Exists")
            return

    # ===== Create Account =====
    User = {
        "Name": Name,
        "ID": ID,
        "PIN": PIN,
        "Balance": Balance
    }

    Users.append(User)
    print("Successfully Created Account ✅")
    time.sleep(3)

# ================== LOGIN ==================
def log_in():
    name = input("Enter Your Name : ").strip().lower()

    for user in Users:
        if user["Name"] == name:
            if authenticate(user):
                print(f"Welcome {user['Name']}")
                print(f"ID : {user['ID']}")
                print(f"Balance : {user['Balance']}")
            return

    print("Account not found")

# ================== DEPOSIT ==================
def deposit_money():
    name = input("Enter Your Name : ").strip().lower()

    for user in Users:
        if user["Name"] == name:
            if authenticate(user):
                try:
                    value = float(input("Enter deposit value : "))
                except ValueError:
                    print("Invalid value")
                    return

                user["Balance"] += value
                print(f"Deposit done. New Balance = {user['Balance']}")
            return

    print("Account not found")

# ================== WITHDRAW ==================
def withdraw():
    name = input("Enter Your Name : ").strip().lower()

    for user in Users:
        if user["Name"] == name:
            if authenticate(user):
                try:
                    value = float(input("Enter withdraw value : "))
                except ValueError:
                    print("Invalid value")
                    return

                if value > user["Balance"]:
                    print("Not enough balance")
                else:
                    user["Balance"] -= value
                    print(f"Withdraw done. New Balance = {user['Balance']}")
            return

    print("Account not found")

# ================== SHOW BALANCE ==================
def show_balance():
    name = input("Enter Your Name : ").strip().lower()

    for user in Users:
        if user["Name"] == name:
            if authenticate(user):
                print(f"Your Balance = {user['Balance']}")
            return

    print("Account not found")

# ================== TRANSFER ==================
def convert_balance():
    sender_name = input("Enter Your Name : ").strip().lower()

    for sender in Users:
        if sender["Name"] == sender_name:
            if not authenticate(sender):
                return

            receiver_name = input("Enter Receiver Name : ").strip().lower()

            if sender_name == receiver_name:
                print("You can't transfer to yourself")
                return

            for receiver in Users:
                if receiver["Name"] == receiver_name:
                    try:
                        value = float(input("Enter transfer value : "))
                    except ValueError:
                        print("Invalid value")
                        return

                    if value > sender["Balance"]:
                        print("Not enough balance")
                        return

                    sender["Balance"] -= value
                    receiver["Balance"] += value
                    print("Transfer completed successfully")
                    return

            print("Receiver not found")
            return

    print("Account not found")

# ================== LOG OUT ==================
def log_out():
    print("Logged out successfully")
    time.sleep(1)

# ================== MENU ==================
def menu():
    while True:
        print("\nATM System")
        print("1 - Create Account")
        print("2 - Log In")
        print("3 - Deposit Money")
        print("4 - Withdraw Money")
        print("5 - Show Balance")
        print("6 - Transfer Balance")
        print("7 - Log Out")
        print("8 - Exit")

        try:
            choice = int(input("Enter Your Choice : "))
        except ValueError:
            print("Numbers only")
            continue

        clear_screen()

        if choice == 1:
            created_account()
        elif choice == 2:
            log_in()
        elif choice == 3:
            deposit_money()
        elif choice == 4:
            withdraw()
        elif choice == 5:
            show_balance()
        elif choice == 6:
            convert_balance()
        elif choice == 7:
            log_out()
        elif choice == 8:
            print("Good Bye 👋")
            break
        else:
            print("Wrong choice")

        time.sleep(3)
        clear_screen()

menu()
