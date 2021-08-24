value = int(input('Введите число: '))

if value < 60:
    sec = value
    print(f"{sec} секунд")
else:
    if value >= 60:
        min = value // 60
        sec = value - min * 60
        if min >= 60:
            hour = min // 60
            min = min - hour * 60
            if hour >= 24:
                day = hour // 24
                hour = hour - day * 24
                print(f"{day} дней {hour} часов {min} минут {sec} секунд")
            else:
                print(f"{hour} часов {min} минут {sec} секунд")
        else:
            print(f"{min} минут {sec} секунд")