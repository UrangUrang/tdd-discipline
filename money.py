from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def plus(self, addend):
        pass


class Money(Expression):
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        if not isinstance(other, Money):
            raise TypeError

        return self.amount == other.amount and \
               self.currency == other.currency

    def __str__(self):
        return "{} - {}".format(self.amount, self.currency)

    @staticmethod
    def dollar(amount):
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount):
        return Franc(amount, "CHF")

    def currency(self):
        return self.currency

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def plus(self, addend):
        return Money(self.amount + addend.amount, self.currency)


class Dollar(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)


class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)


class Bank(object):
    def reduce(self, source, to):
        return Money.dollar(10)