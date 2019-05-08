from money import Dollar


def test_multiplication():
    five = Dollar(5)
    double = five.times(2)
    assert 10 == double
    triple = five.times(3)
    assert 15 == triple
