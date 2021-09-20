import re


def Error_profile(func):
    def wrapper(*args):
        result = func(*args)
        if result is None:
            raise ValueError(*args)
        return result
    return wrapper


@Error_profile
def email_parse(email_address):
    pattern = re.compile(r"(?P<username>\w+)([@])(?P<domain>\w+[.]\w+)")
    result_iter = pattern.finditer(email_address)
    for res in result_iter:
        return res.groupdict()


print(email_parse('geekbrains09@gmail.com'))
