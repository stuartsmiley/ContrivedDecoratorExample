from decorator.activation import register

@register("InchesToCentimeters")
def inches_to_centimeters(value):
    """Converts inches to centimeters"""
    return round(value * 2.54, 2)