from datetime import date, datetime
from collections import defaultdict

users = [{'Jack' : datetime(year=1999, month=6, day=6)},
        {'Peter' : datetime(year=1975, month=6, day=3)},
        {'Anna' : datetime(year=2004, month=6, day=7)},
        {'Jim' : datetime(year=1985,month=6, day=4)},
        {'Sam' : datetime(year=1984, month=6, day=7)},
        {'Alain' : datetime(year=2003,month=6, day=6)}]

def get_birthdays_per_week(user):
    result = defaultdict(list)

    current_date = datetime.now().date().toordinal()
    days_list = []

    for i in range(1, 8):
        day = datetime.fromordinal(current_date + i).date()
        days_list.append(datetime.strftime(day, '%m-%d'))

    for person in users:
        for k, v in person.items():
            d = v.replace(year=2023)
            if datetime.strftime(d, '%m-%d') in days_list:
                if d.weekday() > 4:
                    result['Monday'].append(k)
                else:
                    result[datetime.strftime(d, '%A')].append(k)

    for k, v in sorted(result.items()):
        print (f'{k}: {v}')

get_birthdays_per_week(users)