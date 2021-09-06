import requests

response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")

content = response.content.decode(encoding=response.encoding)


def currency_rates(code):
    currency = {}
    for el, nominal, value in zip(content.split("<CharCode>")[1:], content.split("<Nominal>")[1:], content.split("<Value>")[1:]):
        currency[el.split('<')[0]] = []
        currency[el.split('<')[0]].append(nominal.split('<')[0])
        currency[el.split('<')[0]].append(value.split('<')[0])

    for date in content.split('Date="')[1:]:
        global date_time
        date_time = date.split('"')[0]

    if code in currency:
        rate_list = currency.get(code)
        rate = f"{rate_list[0]} {code} = {rate_list[1]} RUB, {date_time}"
        return rate
    else:
        return None


if __name__ == "__main__":
    pass
