def thesaurus(*args):
    names = {}
    for arg in args:
        value = arg[0]
        if value in names:
            names[value].append(arg)
        else:
            names[value] = list()
            names[value].append(arg)

    print(names)


thesaurus('Ваня', 'Петя', 'Полина', 'Саша', 'Сергей', 'Юля')
