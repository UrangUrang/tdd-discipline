from money import Dollar


def test_multiplication():
    five = Dollar(5)
    five.times(2)
    assert 10 == five.amount
    five.times(3)
    assert 15 == five.amount
