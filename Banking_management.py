class Bank:
    def __init__(self):
        self.users = {}  
        self.loan_active = True
        self.total_balance_in_bank = 0
        self.total_loan_amount_in_bank = 0

    def bank_balance(self):
        return self.total_balance_in_bank

    def total_loan(self):
        return self.total_loan_amount_in_bank

    def bankrupt(self, amount):
        return amount > self.total_balance_in_bank

    def active_loan(self):
        self.loan_active = True
        return "Loan feature is enabled now ."

    def deactive_loan(self):
        self.loan_active = False
        return "Loan feature is disabled now ."


class User:
    def __init__(self, name, bank, bank_name):
        self.name = name
        bank.users[name] = bank_name
        self.balance = 0
        self.transaction_history = []

    def deposit(self, amount, bank):
        self.balance += amount
        bank.total_balance_in_bank += amount
        self.transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount, bank):
        if amount > self.balance:
            return "amount is not available"
        else:
            self.balance -= amount
            bank.total_balance_in_bank -= amount
            self.transaction_history.append(f"Withdrew: {amount}")
            return f"{amount} withdrawn successfully."

    def money_transfer(self, amount, recipient, bank):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            bank.total_balance_in_bank -= amount
            recipient.balance += amount
            self.transaction_history.append(
                f"Transferred: {amount} to {recipient.name}")
            recipient.transaction_history.append(
                f"Received: {amount} from {self.name}")
            return f"{amount} transferred successfully to {recipient.name}"

    def cheak_balance(self):
        return f"Available balance: {self.balance}"

    def taking_loan(self, bank):
        if bank.loan_enabled:
            loan_amount = self.balance * 2
            self.balance += loan_amount
            self.transaction_history.append(f"Loan taken: {loan_amount}")
            bank.total_loan_amount += loan_amount
            return f"Loan of {loan_amount} taken successfully."
        else:
            return "Loan feature is currently disabled."

    def seeing_transaction_history(self):
        return self.transaction_history


class Admin:
    def __init__(self, name):
        self.name = name

    def check_total_bank_balance(self, bank):
        return f"Total available balance: {bank.total_balance_in_bank}"

    def check_total_loan(self, bank):
        return f"Total loan amount: {bank.total_loan_amount_in_bank}"

    def On_Of_loan_feature(self, enable, bank):
        if enable:
            return bank.enable_loan()
        else:
            return bank.disable_loan()


print('Brack_bank')
Brack_bank = Bank()
user1 = User("Alice", Brack_bank, 'Brack_bank')
user2 = User("Bob", Brack_bank, 'Brack_bank')
print(Brack_bank.users)
user1.deposit(1000, Brack_bank)
print(user1.withdraw(700, Brack_bank))
print(user1.money_transfer(200, user2, Brack_bank))
print(user1.cheak_balance())

print("----------------------")

print('Trust_bank')
Trust_bank = Bank()
user3 = User("Nawaz", Trust_bank, 'Trust_bank')
user4 = User("Tushar", Trust_bank, 'Trust_bank')
print(Trust_bank.users)
user3.deposit(500, Trust_bank)
print(user3.withdraw(250, Trust_bank))
print(user3.cheak_balance())

admin = Admin("Admin")
print(admin.check_total_bank_balance(Brack_bank))
print(admin.check_total_bank_balance(Trust_bank))
