workers = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
names = []

for i in workers:
    names.append(i.split()[-1])

n = []
for name in names:
    v = name.lower()
    n.append(v.capitalize())

for v in n:
    print(f"Привет, {v}!")