from converter.miles_to_kilometers import miles_to_kilometers

def test_5k():
    assert miles_to_kilometers(3.1) == 4.99

def test_10k():
    assert miles_to_kilometers(6.2) == 9.98