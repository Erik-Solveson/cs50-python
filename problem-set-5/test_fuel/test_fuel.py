from fuel import convert, gauge

def test_convert():
    assert convert("1/2") == 50
    assert convert("2/2") == 100

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(0) == "E"