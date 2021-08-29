prices = [46.17, 100, 72.63, 25.25, 16, 14.5, 8.27, 1.15, 3, 99, 72.02, 115, 63, 55.55, 13.79]
prices.sort()
rubs = []
cents = []

for i in prices:
    rub = i // 1
    rub = int(rub)
    rubs.append(rub)
    cent = i % 1
    cent = round(cent * 100)
    cents.append((cent))

for rub in rubs:
    ind = rubs.index(rub)
    cent = cents[ind]
    if cent < 10:
        price = f"{rub} руб 0{cent} коп"
        prices.append(price)
    else:
        price = f"{rub} руб {cent} коп"
        prices.append(price)

for n in range(0, 15):
    prices.pop(0)

print(prices)