import re

def class_name_changer(cls, new_name):
    if not re.fullmatch(r'[A-Z][A-Za-z0-9]*', new_name):
        raise Exception("Invalid class name")
    cls.__name__ = new_name
    return cls
