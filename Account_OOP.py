class Account:
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    def deposit(self, amount, password):
        if self.password != password:
            print('Sorry, Wrong password!')
            return None

        elif amount < 0:
            print('You can not deposit a negative amount!')
            return None

        self.balance += amount
        return self.balance

    def withdraw(self, amount, password):
        if self.password != password:
            print('Sorry, wrong password!')
            return None

        elif amount < 0:
            print('You can not withdraw a negative amount!')
            return None

        elif amount > self.balance:
            print('You can not withdraw more than your balance!')
            return None

        self.balance -= amount
        return self.balance

    def getbalance(self, password):
        if self.password != password:
            print('Sorry! Wrong password!')
            return None

        return self.balance

    def show(self):
        print('         Name: ', self.name)
        print('         Balance: ', self.balance)
        print('         Password: ', self.password)