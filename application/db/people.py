from datetime import datetime, date, time

def get_employees():
    d = date(2022, 2, 24)
    t = time(12, 30)
    return print(f' Рандомная дата - {datetime.combine(d, t)}')