
class Money(object):
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        if not isinstance(other, Money):
            raise TypeError

        return self.amount == other.amount and \
               self.__class__ == other.__class__


class Dollar(Money):

    def __init__(self, amount):
        super().__init__(amount)

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)


class Franc(Money):
    def __init__(self, amount):
        super().__init__(amount)

    def times(self, multiplier):
        return Franc(self.amount * multiplier)
