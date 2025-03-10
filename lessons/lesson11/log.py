import logging

logging.basicConfig(filename='example.log',
                    filemode="w",
                    level=logging.ERROR,
                    format='%(asctime)s - %(thread)d - %(levelname)s  - %(filename)s - %(funcName)s - %(message)s')


if __name__ == '__main__':

    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')
