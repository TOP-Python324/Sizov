from datetime import date
from datetime import timedelta as td

def schedule(start_date: date, day: int , *days: int, total_days:int, format_day: str = '%d/%m/%Y') -> list:
    """Генерирует график проведения мероприятий по заданным условиям."""
    
    plan = []

    local_date = start_date
    while total_days > 0:
        plan += [f'{local_date:{format_day}}']
        total_days -= 1
        for next_day in days:
            plan += [f'{local_date + td(days=next_day-day):{format_day}}']
            total_days -= 1
        local_date += td(days=7)

    return plan
    
    