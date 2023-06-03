import datetime


def exception_catcher(func):

    def wrapper(*args, **kwrgs):

        try:
            return func(*args, **kwrgs)
        except Exception as e:
            with open('error_log.txt', "w") as f:
                f.write(f'Exception: {e}\n')
                f.write(f'Exception type: {type(e)}\n')
                f.write(f'Exception time: {datetime.datetime.now()}\n')
                f.write(f'Exception file: {func.__code__.co_filename}\n')
                f.write(f'Exception function: {func.__name__}\n')
                f.write(f'Exception line: {e.__traceback__.tb_lineno}\n')
                f.write('------------------------------------------\n')
                f.close()
                raise e
    return wrapper
