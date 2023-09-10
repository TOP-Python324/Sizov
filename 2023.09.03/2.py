# ДОБАВИТЬ: для типа Decimal есть общеупотребимый псевдоним dec
from decimal import Decimal as dec
from datetime import time
from datetime import date
from datetime import datetime as dt
from numbers import Number


class PowerMeter:
    """
    Описывает двухтарифный счётчик потреблённой электрической мощности.
    """
    # ИСПОЛЬЗОВАТЬ: в большинстве случаев аннотацию возвращаемых значений встроенных методов можно опустить
    # ИСПРАВИТЬ: согласно условию, конструктор должен предоставить возможность передать четыре аргумента
    def __init__(self, tariff1: dec = 5.28, tariff2: dec = 2.5, tariff2_starts: time = time(23,00), tariff2_ends: time = time(7,00)):
        # ИСПРАВИТЬ: при использовании инструкции from ... import ... в глобальное пространство имён добавляется идентификатор импортированного объекта, а идентификатор модуля не добавляется — следовательно использовать имена decimal и datetime мы не можем
        self.tariff1 = dec(tariff1)
        self.tariff2 = dec(tariff2)
        self.tariff2_starts = tariff2_starts
        self.tariff2_ends = tariff2_ends
        self.power: dec = 0
        self.charges: dict[date, dec] = {}
        
    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.power} кВт/ч>'
    
    def __str__(self):
        today = date.today()
        try:
            # ИСПРАВИТЬ: а если ключа в словаре нет? (см. тест ниже)
            # ИСПРАВИТЬ: нас интересует текущий месяц, а не следующий
            return f'({today:%B}) {self.charges[date(today.year, today.month, 1)]}'  
        except KeyError:
            return 'Данные отсутствуют!'
        
    def meter(self, power: Number) -> dec:
        """Вычисляет и возвращает стоимость согласно тарифному плану, действующему в текущий момент."""
        current_date_time = dt.now()
        current_time = current_date_time.time()

        # если дневной тариф
        # ИСПОЛЬЗОВАТЬ: представьте числовую ось, поместите на ней метки tariff2_starts и tariff2_ends (вторая явно окажется правее), теперь нанесите на ось отметки current_time для истинного условия — в каком порядке у вас окажутся подписи меток, в таком же порядке записывайте неравенства — так станет куда проще воспринимать условие целиком
        if self.tariff2_ends < current_time < self.tariff2_starts:
            value = round(dec(power)*self.tariff1, 2)
        else:
            value = round(dec(power)*self.tariff2, 2)

        # ИСПРАВИТЬ: используйте словарные методы get() и setdefault() вместо явной проверки наличия ключа
        # ИСПРАВИТЬ: нас интересует текущий месяц, а не следующий                
        self.charges.setdefault(date(current_date_time.year, current_date_time.month, 1), 0)
        self.charges[date(current_date_time.year, current_date_time.month, 1)] += value

        self.power += power
        return value


# >>> pm1 = PowerMeter()
# >>> pm1.meter(2)
# Decimal('10.56')
# >>> pm1.meter(1.2)
# Decimal('6.34')
# >>>
# >>> pm1
# <PowerMeter: 3.2 кВт/ч>
# >>>
# >>> print(pm1)
# (August) 6.34

# >>> pm1 = PowerMeter()
# >>> print(pm1)
# ...
#     return f'({today:%B}) {self.charges[date(today.year, today.month+1, 1)]}'
#                            ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# KeyError: datetime.date(2023, 9, 1)


# ИТОГ: надо лучше, доработать — 4/7

# >>> pm1 = PowerMeter()
# >>> pm1.meter(2)
# Decimal('10.56')
# >>> pm1.meter(1.2)
# Decimal('6.34')
# >>>
# >>> pm1
# <PowerMeter: 3.2 кВт/ч>
# >>>
# >>> print(pm1)
# (August) 16.90
# >>>
# >>> pm1 = PowerMeter()
# >>> print(pm1)
# Данные отсутствуют!
