import plates as p

def test_character_count(): #test counts 1,7,4
    assert p.contains_character_count('a') == False
    assert p.contains_character_count('aaaaaaa') == False
    assert p.contains_character_count('aaaa') == True

def test_starting_letters():
    assert p.contains_starting_letters('11abc') == False
    assert p.contains_starting_letters('abc') == True
    assert p.contains_starting_letters('1abc') == False

def test_contains_numbers():
    assert p.contains_numbers('abcd') == True
    assert p.contains_numbers('abcd12') == True
    assert p.contains_numbers('abc12d') == False
    assert p.contains_numbers('abc12D') == False

def test_contains_no_punctuation():
    assert p.contains_no_punctuation('abcd') == True
    assert p.contains_no_punctuation('abcd.') == False
    assert p.contains_no_punctuation('.') == False