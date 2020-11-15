####################################################
####################################################
# Object Oriented Programming Challenge - Solution
####################################################
####################################################
#
# For this challenge, create a bank account class that has two attributes:
#
# * owner
# * balance
#
# and two methods:
#
# * deposit
# * withdraw
#
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.




class Account:

    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        return (f"Owner: {self.owner}\nBalance: {self.balance}")


    def deposit(self,amount):
        self.balance+=amount
        print (f"Your account has been credited by {amount}")

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"Your account has been debited by {amount} and current account balance is {self.balance}")
        else:
            print("sorry you don't have this much of money in your account")

# 1. Instantiate the class
acct1 = Account('Jose',100)
acct1.deposit(400)
acct1.withdraw(200)
acct1.withdraw(500)

# 2. Print the object
print(acct1)




# 3. Show the account owner attribute
print(acct1.owner)




# 4. Show the account balance attribute
print(acct1.balance)




# 5. Make a series of deposits and withdrawals
acct1.deposit(50)




acct1.withdraw(75)




# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)



# ## Good job!
