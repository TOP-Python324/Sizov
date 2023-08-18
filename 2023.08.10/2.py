# ДОБАВИТЬ: для типа Decimal есть общеупотребимый псевдоним dec
from decimal import Decimal
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
    def __init__(self):
        # ИСПРАВИТЬ: при использовании инструкции from ... import ... в глобальное пространство имён добавляется идентификатор импортированного объекта, а идентификатор модуля не добавляется — следовательно использовать имена decimal и datetime мы не можем
        self.tariff1: decimal.Decimal = 5.28
        self.tariff2: decimal.Decimal = 2.5
        self.tariff2_starts: datetime.time = time(23,00)
        self.tariff2_ends: datetime.time = time(7,00)
        self.power: decimal.Decimal = 0
        self.charges: dict[datetime.date, decimal.Decimal] = {}
        
    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.power} кВт/ч>'
    
    def __str__(self):
        today = date.today()
        if today.month == 12:
            # ИСПРАВИТЬ: а если ключа в словаре нет? (см. тест ниже)
            # ИСПРАВИТЬ: нас интересует текущий месяц, а не следующий
            return f'({today:%B}) {self.charges[date(today.year+1, 1, 1)]}'  
        else:
            return f'({today:%B}) {self.charges[date(today.year, today.month+1, 1)]}'
        
    def meter(self, power: Number) -> Decimal:
        """Вычисляет и возвращает стоимость согласно тарифному плану, действующему в текущий момент."""
        current_date_time = dt.now()
        current_time = current_date_time.time()

        # если дневной тариф
        # ИСПОЛЬЗОВАТЬ: представьте числовую ось, поместите на ней метки tariff2_starts и tariff2_ends (вторая явно окажется правее), теперь нанесите на ось отметки current_time для истинного условия — в каком порядке у вас окажутся подписи меток, в таком же порядке записывайте неравенства — так станет куда проще воспринимать условие целиком
        if current_time < self.tariff2_starts or self.tariff2_ends < current_time:
            value = round(Decimal(power*self.tariff1), 2)
        else:
            value = round(Decimal(power*self.tariff2), 2)

        if current_date_time.month == 12:
            # ИСПРАВИТЬ: используйте словарные методы get() и setdefault() вместо явной проверки наличия ключа
            if date(current_date_time.year+1, 1, 1) in self.charges:
                # ИСПРАВИТЬ: нас интересует текущий месяц, а не следующий
                self.charges[date(current_date_time.year+1, 1, 1)] += value
            else:
                self.charges[date(current_date_time.year+1, 1, 1)] = value
        else:
            if date(current_date_time.year+1, 1, 1) in self.charges:
                self.charges[date(current_date_time.year, current_date_time.month+1, 1)] += value
            else:
                self.charges[date(current_date_time.year, current_date_time.month+1, 1)] = value

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
