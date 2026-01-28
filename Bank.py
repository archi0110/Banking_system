class Bank:
    def __init__(self, name, acc_no, pin, balance=0):
        self.name = name
        self.acc_no = acc_no
        self.pin = pin
        self.balance = balance
        self.history = []

    def login(self):
        for _ in range(3):
            entered_pin = input("Enter PIN: ")
            if entered_pin == self.pin:
                print("Login Successful\n")
                return True
            else:
                print("Wrong PIN")
        print("Account Locked!")
        return False

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return
        self.balance += amount
        self.history.append(f"Deposited {amount}")
        print(f"{amount} deposited")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return
        if amount > 10000:
            print("Daily withdraw limit is ₹10,000")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            self.history.append(f"Withdrawn {amount}")
            print(f"{amount} withdrawn")

    def check_balance(self):
        print(f"Balance: {self.balance}")

    def mini_statement(self):
        print("\n Mini Statement (Last 5 Transactions)")
        for t in self.history[-5:]:
            print("-", t)

    def display(self):
        print("\n========== ACCOUNT DETAILS ==========")
        print("Name       :", self.name)
        print("Account No :", self.acc_no)
        print("Balance    :", self.balance)
        


# -------- MAIN PROGRAM --------
account = Bank("Archi Patel", 43567, "1234", 5000)

if account.login():
    while True:
        print("""
1. Deposit
2. Withdraw
3. Check Balance
4. Mini Statement
5. Account Details
6. Exit
""")
        choice = input("Enter your choice: ")

        if choice == "1":
            account.deposit(int(input("Enter amount: ")))

        elif choice == "2":
            account.withdraw(int(input("Enter amount: ")))

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            account.mini_statement()

        elif choice == "5":
            account.display()

        elif choice == "6":
            print("Thank you.....!")
            break

        else:
            print("Invalid choice")
