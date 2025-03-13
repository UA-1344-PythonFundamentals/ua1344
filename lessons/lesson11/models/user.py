from log import logging

class User:
    __id = 0
    def __init__(self, username, password):
        self.id = self.__get_id()
        if not username:
            raise ValueError('Username cannot be empty')
        self.username = username
        if not password:
            raise ValueError('Password cannot be empty')
        self.password = password
        logging.info(f'User id:{id} {self.username} created')

    def __str__(self):
        return f'{self.username}'

    def __repr__(self):
        return f'<User {self.id} {self.username}>'
    def __del__(self):
        logging.info(f'User id:{id} {self.username} deleted')
    
    @classmethod
    def __get_id(cls):
        cls.__id += 1
        return cls.__id