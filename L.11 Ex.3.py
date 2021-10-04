class NotDigit(Exception):
    pass


digits = []
user_input = 0
while user_input != 'stop':
    user_input = input('Введите число: ')
    try:
        if user_input.isdigit():
            user_input = int(user_input)
            digits.append(user_input)
        else:
            raise NotDigit('Введенная строка не является числом!!!')
    except (TypeError, NotDigit) as err:
        print(err)

print(digits)
