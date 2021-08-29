inf = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

inf.remove('5')
inf.remove('+5')
inf.insert(1, '05')
inf.insert(-2, '+05')

inf.insert(1, '"')
inf.insert(3, '"')
inf.insert(5, '"')
inf.insert(7, '"')
inf.insert(11, '"')
inf.insert(13, '"')

output = ''

for i in inf:
    output = output + i + ' '

print(output)