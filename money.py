class Dollar(object):

    def __init__(self, amount):
        self.__amount = amount

    def times(self, multiplier):
        return Dollar(self.__amount * multiplier)

    def __eq__(self, other):
        if not isinstance(other, Dollar):
            raise TypeError
        return self.__amount == other.__amount


class Franc(object):
    def __init__(self, amount):
        self.__amount = amount

    def times(self, multiplier):
        return Franc(self.__amount * multiplier)

    def __eq__(self, other):
        if not isinstance(other, Franc):
            raise TypeError
        return self.__amount == other.__amount
