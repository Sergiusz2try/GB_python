numbers = []

for i in range(1, 1000):
    if i % 2 != 0:
        numbers.append(i ** 3)

sum_numbers = []

for num in numbers:
    num_str = str(num)
    sum_num = 0
    for n in num_str:
        sum_num += int(n)
    if sum_num % 7 == 0:
        sum_numbers.append(num)

sum_value1 = 0
for n in sum_numbers:
    sum_value1 += n

print("Сумма первого случая: ", sum_value1)

sum_numbers = [i + 17 for i in sum_numbers]
sum_numbers2 = []

for number in sum_numbers:
    num_str = str(number)
    sum_num = 0
    for n in num_str:
        sum_num += int(n)
    if sum_num % 7 == 0:
        sum_numbers2.append(number)

sum_value2 = 0
for v in sum_numbers2:
    sum_value2 += v

print("Сумма чисел второго случая: ", sum_value2)
