from converter.ounces_to_grams import OuncesToGrams

def test_oz_to_grams_for_one():
    converter = OuncesToGrams()
    assert converter.convert(1) == 28.3495