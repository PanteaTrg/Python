class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    def deposit(self, password, amount):
        if password != self.password:
            print('Wrong password')
            return None
        if amount < 0:
            print('You can not deposit a negative amount')
            return None
        self.balance += amount
        return self.balance

    def withdraw(self, password, amount):
        if password != self.password:
            print('Wrong password')
            return None
        if amount > self.balance:
            print('You can not withdraw more than your balance')
            return None
        if amount < 0:
            print('You can not withdraw a negative amount')
            return None
        self.balance -= amount
        return self.balance

    def getBalance(self, password):
        if password != self.password:
            print('Wrong password')
            return None
        return self.balance

    def show(self):
        print('Name: ', self.name)
        print('Balance: ', self.balance)
        print('Password: ', self.password)
        print()


# Creating an object from Account class:
my_account = Account('Pantea', 10000, '123')
my_account.show()
print(my_account.deposit('123', 5000))
my_account.withdraw('1', 12)