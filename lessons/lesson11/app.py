from models.user import User
from log import logging
from utils import generate_random_string
from random import randint
from pprint import pprint


users = []

while len(users) < 10:
    username = generate_random_string(randint(5, 10))
    password = generate_random_string(randint(5, 10))
    try:
        user = User(username, password)
    except ValueError as e:
        logging.error(e)
    else:
        users.append(user)

pprint(users)