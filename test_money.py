from money import Dollar, Franc


def test_multiplication():
    five = Dollar(5)
    assert Dollar(10) == five.times(2)
    assert Dollar(15) == five.times(3)


def test_franc_multiplication():
    five = Franc(5)
    assert Franc(10) == five.times(2)
    assert Franc(15) == five.times(3)


def test_equality():
    assert Dollar(5).__eq__(Dollar(5)) is True
    assert (Dollar(5) == Dollar(5)) is True
    assert Dollar(5).__eq__(Dollar(6)) is False
    assert (Dollar(5) == Dollar(6)) is False

