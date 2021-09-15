import sys

args = sys.argv
print(args)
with open('bakery.csv', 'r', encoding='utf-8') as f:
    if len(args) == 1:
        for row in f:
            print(row, end='')
    elif len(args) == 2:
        n = int(args[1])
        for row in f:
            if n != 1:
                n -= 1
                continue
            print(row, end='')
    elif len(args) == 3:
        n = int(args[1])
        m = int(args[2])
        for row in f:
            if n != 1:
                n -= 1
                continue
            print(row, end='')
            m -= 1
            if m == 1:
                break
    else:
        print('Error')
