from log import logging
import random
import string

def generate_random_string(length):
    if length < 0:
        logging.error(f'Length should be greater than 0, length: {length}')
        return None
    value =''.join(random.choices(string.ascii_letters + string.digits, k=length))
    logging.debug(f'Generating random string of length: {length} value: {value}')

    return value