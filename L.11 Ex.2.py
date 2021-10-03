class ZeroDivErr(Exception):
    pass


division = input()
try:
    division = division.split('/')
    if division[-1] == '0':
        raise ZeroDivErr("На 0 делить нельзя!!!")
    else:
        print(int(division[0]) / int(division[1]))
except (ValueError, ZeroDivErr) as err:
    print(err)

