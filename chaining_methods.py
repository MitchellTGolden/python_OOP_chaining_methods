class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        self.display_balance = print(f"{self.name}, Your current balance is : {self.account_balance} Dollars") 
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self
mitchell = User("Mitchell Golden", "aRealEmail@mail.com")
adrien = User("Adrien Dion", "LiteralRubixGod@mail.com")
anne = User("Anne Jurack", "Anneimations@mail.com")

mitchell.make_deposit(100).make_deposit(200).make_deposit(500).make_withdrawl(300).display_user_balance()
adrien.make_deposit(1000).make_deposit(500).make_withdrawl(500).make_withdrawl(500).display_user_balance()
anne.make_deposit(100000).make_withdrawl(1100).make_withdrawl(900).make_withdrawl(8000).display_user_balance()
mitchell.transfer_money(adrien, 502).display_user_balance()
adrien.display_user_balance()