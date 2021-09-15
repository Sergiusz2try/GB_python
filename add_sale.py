import sys

arg = sys.argv[1]
with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.write(arg)
    f.write('\n')
