import random
import string
from typing import List, Optional, Dict, Any

class User:
    """A class representing a user."""
    __pk = 0
    def __init__(self, username: str, email: str, password: str, full_name: Optional[str] = None, is_active: bool = True):
        self.pk = self.__get_pk() # Primary Key
        self.username = username
        self.email = email
        self.password = password
        self.full_name = full_name
        self.is_active = is_active

    def __str__(self) -> str:
        return f"User(id={self.pk}, username='{self.username}', email='{self.email}', full_name='{self.full_name}', active={self.is_active})"

    def disable(self) -> None:
        self.is_active = False

    def enable(self) -> None:
        self.is_active = True
    
    def update_full_name(self, new_full_name: str) -> None:
        self.full_name = new_full_name

    def check_password(self, password_to_check: str) -> bool:
        return self.password == password_to_check # Never do this in production.
    @classmethod
    def __get_pk(cls)->int:
        cls.__pk += 1
        return cls.__pk
    
    def to_dict(self) -> Dict[str, Any]:
        """Returns a dictionary representation of the User object."""
        return {
            "pk": self.pk,
            "username": self.username,
            "email": self.email,
            "full_name": self.full_name,
            "is_active": self.is_active,
        }

def generate_users(num_users: int = 10) -> List[User]:
    """Generates a list of random User objects."""
    users: List[User] = []
    for i in range(num_users): # i is now the ID
        username = ''.join(random.choices(string.ascii_lowercase, k=8))
        email = f"{username}@example.com"
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=12)) # Again, hash this in real use.
        full_name = f"{username.capitalize()} User"
        user = User(username, email, password, full_name) # IDs start at 1.
        users.append(user)
    return users



if __name__ == "__main__":
    # Example usage:
    random_users = generate_users(5)
    for user in random_users:
        print(user)

    # Example of using the generated users
    random_users[0].disable()
    print(random_users[0])

    random_users[1].update_full_name("New Name")
    print(random_users[1])

    print(random_users[2].check_password(random_users[2].password)) #Never do this in production