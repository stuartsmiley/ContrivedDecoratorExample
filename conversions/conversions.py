from decorator.activation import activate
# these imports are required to get the converters registered
# a linter won't be happy with them...
import converter.miles_to_kilometers
import converter.inches_to_centimeters
import converter.fahrenheit_to_celsius
import converter.ounces_to_grams

print("32 F equals " + str(activate(32, "FahrenheitToCelsius")) + " in celsius")

print("3.1 miles equals " + str(activate(3.1, "MilesToKilometers")) + " in km")

print("72 F equals " + str(activate(72, "FahrenheitToCelsius")) + " in celsius")

print("10 inches equals " + str(activate(10, "InchesToCentimeters")) + " in centimeters")

print("4 oz equals "  + str(activate(4, "OuncesToGrams")) + " in grams")