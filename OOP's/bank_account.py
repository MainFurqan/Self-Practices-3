class BankAccount:
    def __init__(self, name, account_no, balance=100000): 
        self.name = name
        self.account_no = account_no
        self.balance = balance  # Now balance is an instance variable

    def debit(self, amount):
        if amount > self.balance:
            print("❌ Insufficient balance! Transaction failed.")
        else:
            self.balance -= amount
            print(f"✅ Transaction successful! ₹{amount} debited.")
            print(f" Remaining Balance: ₹{self.balance}")

    def credit(self, amount):
        self.balance += amount
        print(f"✅ Transaction successful! ₹{amount} credited.")
        print(f" Updated Balance: ₹{self.balance}")

def main():
    # Get user details
    name = input("Enter Name: ")
    account_no = input("Enter Account No: ")
    account = BankAccount(name, account_no)  

    while True:
        print("\n🔹 Choose an action:")
        print("1️⃣ Debit Money")
        print("2️⃣ Credit Money")
        print("3️⃣ Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to debit: ₹"))
            account.debit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to credit: ₹"))
            account.credit(amount)
        elif choice == "3":
            print("✅ Thank you for banking with us!")
            break
        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")

# Run the program
main()
