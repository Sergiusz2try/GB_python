def num_translate_adv(number):
    translator = {
        'One': 'Один',
        'one': 'один',
        'Two': 'Два',
        'two': 'два',
        'Three': 'Три',
        'three': 'три',
        'Four': 'Четыре',
        'four': 'четыре',
        'Five': 'Пять',
        'five': 'пять',
        'Six': 'Шесть',
        'six': 'шесть',
        'Seven': 'Семь',
        'seven': 'семь',
        'Eight': 'Восемь',
        'eight': 'восемь',
        'Nine': 'Девять',
        'nine': 'девять',
        'Ten': 'Десять',
        'ten': 'десять'
    }

    if number in translator:
        translate_num = translator[number]
        print(translate_num)
    else:
        print('None')


num = input('Введите число которое хотите перевести: ')
num_translate_adv(num)
