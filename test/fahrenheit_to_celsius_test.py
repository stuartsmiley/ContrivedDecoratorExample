from converter.fahrenheit_to_celsius import fahrenheit_to_celsius

def test_fahrenheit_to_celsius_for_freezing():
    assert fahrenheit_to_celsius(32) == 0

def test_conversion_for_boiling():
    assert fahrenheit_to_celsius(212) == 100

def test_room_temperature_conversion():
    assert fahrenheit_to_celsius(72) == 22

def test_slightly_warmer_room_temperature_conversion():
    assert fahrenheit_to_celsius(74) == 23