from twttr import shorten

def test_vowels():
    assert shorten('Hello') == "Hll"

def test_uppercase():
    assert shorten("HELLO") == "HLL"

