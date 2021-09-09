tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Анна'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]


def students_klass(students, klass):
    if len(students) <= len(klass):
        for student, kls in zip(students, klass):
            output = (student, kls)
            yield output
    else:
        lens = len(students) - len(klass)
        for i in range(1, lens + 1):
            klass.append('None')
        for student, kls in zip(students, klass):
            output = (student, kls)
            yield output


go_klasses = students_klass(tutors, klasses)
print(next(go_klasses))
print(next(go_klasses))
print(next(go_klasses))
print(next(go_klasses))
print(next(go_klasses))
print(next(go_klasses))
print(next(go_klasses))
print(next(go_klasses))
print(next(go_klasses))
