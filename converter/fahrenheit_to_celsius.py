from decorator.activation import register

@register("FahrenheitToCelsius")
def fahrenheit_to_celsius(value):
    """Converts a Fahrenheit temperature to a Celsius temperature"""
    return round((value - 32) * 5.0/9.0)