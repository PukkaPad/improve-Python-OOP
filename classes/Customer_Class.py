# -*- coding: utf-8 -*-

class Customer (object):
    """A customer of a Bank with a checking account. The properties of customers are:
    Attributes:
    name: A string representing the name
    balance: a float tracking the current balance
    """

    def __init__(self, name, balance =0.0):
        """Return a Customer object whose name is *name* and starting balance is *balance*."""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balancing remaining after withdrawing *amount* $."""
        if amount > self.balance:
            raise RuntimeError ('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount* dollars."""
        self.balance += amount
        return self.balance


peter = Customer('Peter Milk', 220730.0)
print (peter.withdraw(55685))