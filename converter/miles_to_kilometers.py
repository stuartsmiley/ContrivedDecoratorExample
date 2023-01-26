from decorator.activation import register

@register("MilesToKilometers")
def miles_to_kilometers(value):
    """Converts a distance in miles to a distance in kilometers"""
    return round((value * 1.609344), 2)