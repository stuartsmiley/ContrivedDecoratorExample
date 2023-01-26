from converter.converter import ConverterInterface
from decorator.activation import register

@register("OuncesToGrams")
class OuncesToGrams(ConverterInterface):
    def __init__(self):
        self.conversionFactor = 28.3495

    def convert(self, value):
        return value * self.conversionFactor