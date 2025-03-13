def change_class_name(cls, new_name):
    if not new_name[0].isupper():
        raise ValueError("Class name must start with an uppercase letter")
    if not new_name.isalnum():
        raise ValueError("Class name must contain only alphanumeric characters")
    
    cls.__name__ = new_name
    return cls

class MyClass:
    pass

# Test cases
if __name__ == "__main__":
    # Valid renaming
    MyClass = change_class_name(MyClass, "UsefulClass")
    print(MyClass.__name__)  # Outputs: UsefulClass

    MyClass = change_class_name(MyClass, "SecondUsefulClass")
    print(MyClass.__name__)

    try:
        change_class_name(MyClass, "usefulClass")
    except ValueError as e:
        print(e)

    try:
        change_class_name(MyClass, "Useful_Class")
    except ValueError as e:
        print(e)