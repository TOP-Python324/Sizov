from datetime import date
from datetime import timedelta as td

def schedule(start_date: date, day: int , *days: int, total_days:int, format_day: str = '%d/%m/%Y') -> list:
    """Генерирует график проведения мероприятий по заданным условиям."""

    plan = []
    weekdays = [day]
    for day in days:
        weekdays.append(day)

#    if 'vacations' in globals():
#        print('yes')
    while total_days > 0:
        if start_date.isoweekday() in weekdays:
            plan += [f'{start_date:{format_day}}']
            total_days -= 1
        start_date += td(days=1)

    return plan
    
    