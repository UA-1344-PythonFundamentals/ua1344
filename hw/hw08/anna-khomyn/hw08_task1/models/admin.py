__all__ = ["create_admin"]

__admin_name = "Anna"

def create_admin(name):
    global __admin_name
    print(f"Greeting from admin {__admin_name}! \n\t==>> Creating admin {name}\n")
    __admin_name = name

def delete_admin():
    pass