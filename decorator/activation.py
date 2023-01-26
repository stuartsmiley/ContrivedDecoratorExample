from converter.converter import ConverterInterface

ACTIVATION = {}

def register(name):
    print("registering " + name)
    def decorator(fn):
        # assign converter to "name" key in ACTIVATION
        if isinstance(fn, type):
            ACTIVATION[name] = fn()
        else:
            ACTIVATION[name] = fn
        # return converter unmodified
        return fn
    return decorator

def activate(value, kind):
    try:
        fn = ACTIVATION[kind]
        if issubclass(type(fn), ConverterInterface):
            return fn.convert(value)
        return fn(value)
    except KeyError:
        print("Activation function/class %s undefined" % kind)
