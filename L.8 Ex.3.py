def type_logger(func):
    def wrapper(*args):
        res = func(*args)
        print(res)
        return type(res)
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
