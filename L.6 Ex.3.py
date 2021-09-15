with open('users.csv', encoding='utf-8') as users, open('hobby.csv', encoding='utf-8') as hobby:
    users_list = []
    for row in users:
        for el in row.split(','):
            users_list.append(el)

    hobby_list = []
    for row in hobby:
        for el in row.split(','):
            hobby_list.append(el)

    if len(users_list) >= len(hobby_list):
        if len(users_list) > len(hobby_list):
            for _ in range(1, len(users_list) - len(hobby_list) + 1):
                hobby_list.append('None')
        users_hobby = {}
        for key, value in zip(users_list, hobby_list):
            users_hobby[key] = value
        print(users_hobby)
    else:
        print('Error: 1')
