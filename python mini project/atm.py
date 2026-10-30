balance = 10000

def check_balance():
    print("Available Balance: ₹", balance)


def deposit():
    global balance
    amount = float(input("Enter amount to deposit: ₹"))

    if amount <= 0:
        print("Invalid amount")
    else:
        balance += amount
        print("Amount deposited successfully!")
        print("Current Balance: ₹", balance)


def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: ₹"))

    if amount <= 0:
        print("Invalid amount! Enter a positive amount.")
    elif amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        print("Please collect your cash.")
        print("Remaining Balance: ₹", balance)


def show_menu():
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        print("Thank you for using our ATM!")
        break

    else:
        print("Invalid choice")
