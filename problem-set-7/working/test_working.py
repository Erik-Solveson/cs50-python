import working

def test_convert():
    assert working.convert('9 AM to 5 PM') == "09:00 to 17:00"
    assert working.convert('10 AM to 8:50 PM')
    assert working.convert('10:30 PM to 8 AM')
    assert working.convert('9:00 AM to 5:00 PM')
    assert working.convert('9:00 AM to 5:00 PM')
    assert working.convert('9:00 AM to 5:00 PM')