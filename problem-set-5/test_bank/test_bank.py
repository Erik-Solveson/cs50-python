from bank import value

def test_hello():
    assert value('hello') == "$0"

def test_whatsup():
    assert value("What's up?") == "$100"

def test_Hi():
    assert value("Hi") == "$20"