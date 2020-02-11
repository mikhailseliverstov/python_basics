class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def extract(cls, date):
        # print(date)
        print(list(map(int, date.split('-'))))
        # print(l)


    @staticmethod
    def validate(date):
        ymd = date.split('-')
        try:
            if int(ymd[1]) < 1 or int(ymd[1]) > 12:
                raise OwnError("Номер месяца должен быть от 1 до 12")
            elif int(ymd[0]) < 1 or int(ymd[0]) > 31:
                raise OwnError("День месяца должен быть от 1 до 31")
            elif int(ymd[1]) == 2 and int(ymd[0]) > 29:
                raise OwnError("В ноябре не может быть больше 29 дней")
            elif int(ymd[1]) in (4, 6, 9, 11) and int(ymd[0]) >30:
                raise OwnError("В апреле, июне, сентябре и ноябре не больше 30 дней")
        except OwnError as err:
            print(err)



Date.validate('31-19-2019')
Date.validate('0-1-2019')
Date.validate('30-02-2019')
Date.validate('31-9-2019')
Date.extract('31-12-2020')
