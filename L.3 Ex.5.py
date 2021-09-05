import random


def get_jokes(n):
    """
    Returning n jokes formed from three random words taken from three lists (one from each)
    :param n: number of jokes
    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    jokes = []
    joke = ""
    for i in range(n):
        noun = random.choice(nouns)
        nouns.remove(noun)
        adv = random.choice(adverbs)
        adverbs.remove(adv)
        adj = random.choice(adjectives)
        adjectives.remove(adj)

        joke = noun + ' ' + adv + ' ' + adj
        jokes.append(joke)

    print(jokes)


number = int(input("Введите кол-во шуток: "))
if number < 6:
    number = number
else:
    while number >= 6:
        number = int(input("Введенное значение слишком велико, введите значение от 1 до 5: "))

get_jokes(number)
