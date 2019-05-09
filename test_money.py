from money import Dollar


def test_multiplication():
    five = Dollar(5)
    double = five.times(2)
    assert 10 == double.amount
    triple = five.times(3)
    assert 15 == triple.amount


def test_equality():
    assert Dollar(5).__eq__(Dollar(5)) is True
    assert (Dollar(5) == Dollar(5)) is True
    assert Dollar(5).__eq__(Dollar(6)) is False
    assert (Dollar(5) == Dollar(6)) is False

