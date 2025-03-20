import re

def сменить_имя_класса(cls, новое_имя):
    if not re.fullmatch(r'[A-Z][A-Za-z0-9]*', новое_имя):
        raise Exception("Неверное имя класса")
    cls.__name__ = новое_имя
    return cls
