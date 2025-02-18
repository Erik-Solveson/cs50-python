import um

def test_count():
    assert um.count('um') == 1
    assert um.count('Um, hello') == 1
    assert um.count("hello") == 'no "um"s found'



    'no "um"s found'