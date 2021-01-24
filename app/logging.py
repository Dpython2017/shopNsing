import logging
logging.basicConfig(filename="app.log", level=logging.INFO)


def logs(func):
    def log_func(*args):
        logging.info('Running method {} , response is:{}'.format(func.__name__, args))
    return log_func