class Account:
    def __init__(self, owner, balance):
        self.owner = owner.split()
        self.balance = balance

    def deposit(self, dep):
        if dep > 0:
            self.balance += dep
            print("Succesfully deposited", dep)
        else:
            print("______________")
            print("Deposit error")

    def withdraw(self, wth):
        if wth < self.balance and wth > 0:
            self.balance -= wth
            print("Successfully withdrew", wth)
        else:
            print("____________________")
            print("Operation is denied")

    def show(self):
        print("_____________")
        for i in self.owner:
            print(i, end=" ")
        print()
        print(self.balance)
s, bal = input(), float(input())
acc = Account(s, bal)
wth = float(input())
acc.withdraw(wth)
de = float(input())
acc.deposit(de)
