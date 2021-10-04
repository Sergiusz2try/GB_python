class Date:
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return f'{self.date}'

    @classmethod
    def get(cls, date):
        date = date.split('-')
        date = [int(x) for x in date]
        return date

    @staticmethod
    def validation_date(date):
        date = date.split('-')
        date = [int(x) for x in date]
        if (date[1] >= 1) and (date[1] <= 12):
            pass
        else:
            raise ValueError

        if (date[2] >= 2000) and (date[2] <= 2050):
            pass
        else:
            raise ValueError


date_1 = Date('10-03-2001')
print(date_1.get('10-03-2001'))
date_1.validation_date('10-12-2001')
