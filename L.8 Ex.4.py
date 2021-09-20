def val_checker(cond=0):
    def _val_checker(func):
        def wrapper(arg):
            if arg < cond:
                raise ValueError(arg)
            else:
                res = func(arg)
            return res
        return wrapper
    return _val_checker


@val_checker(10)
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
