from money import Dollar, Franc


def test_multiplication():
    five = Dollar(5, "USD")
    assert Dollar(10, "USD") == five.times(2)
    assert Dollar(15, "USD") == five.times(3)


def test_franc_multiplication():
    five = Franc(5, "CHF")
    assert Franc(10, "CHF") == five.times(2)
    assert Franc(15, "CHF") == five.times(3)


def test_equality():
    assert (Dollar(5, "USD") == Dollar(5, "USD")) is True
    assert (Dollar(5, "USD") == Dollar(6, "USD")) is False
    assert (Franc(5, "CHF") == Franc(5, "CHF")) is True
    assert (Franc(5, "CHF") == Franc(6, "CHF")) is False

    assert (Franc(5, "CHF") == Dollar(5, "USD")) is False
    assert (Franc(5, "CHF") == Dollar(6, "USD")) is False


def test_currency():
    assert Dollar(5, "USD").currency is "USD"
    assert Franc(5, "CHF").currency is "CHF"