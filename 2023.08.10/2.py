from decimal import Decimal
from datetime import time
from datetime import date
from datetime import datetime as dt
from numbers import Number

class PowerMeter:
    """ Описывает двухтарифный счётчик потреблённой электрической мощности."""
    
    # конструктор
    def __init__(self) -> None:
        # атрибуты экземпляра
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
            return f'({today:%B}) {self.charges[date(today.year+1, 1, 1)]}'  
        else:
            return f'({today:%B}) {self.charges[date(today.year, today.month + 1, 1)]}'
        
    def meter(self, power: Number) -> Decimal:    
        """ Вычисляет и возвращает стоимость согласно тарифному плану, действующему в текущий момент"""
        current_date_time = dt.now()
        current_time = current_date_time.time()

        # если дневной тариф
        if current_time > self.tariff2_ends or current_time < self.tariff2_starts:
            value = round(Decimal(power*self.tariff1), 2)
        else:
            value = round(Decimal(power*self.tariff2), 2)
        
        if current_date_time.month == 12:
            if date(current_date_time.year+1, 1, 1) in self.charges:                
                self.charges[date(current_date_time.year+1, 1, 1)] += value
            else:
                self.charges[date(current_date_time.year+1, 1, 1)] = value
        else:
            if date(current_date_time.year+1, 1, 1) in self.charges: 
                self.charges[date(current_date_time.year, current_date_time.month + 1, 1)] += value
            else:
                self.charges[date(current_date_time.year, current_date_time.month + 1, 1)] = value
        
        self.power +=  power   
        return value    
        
#>>> pm1 = PowerMeter()
#>>> pm1.meter(2)
#Decimal('10.56')
#>>> pm1.meter(1.2)
#Decimal('6.34')
#>>>
#>>> pm1
#<PowerMeter: 3.2 кВт/ч>
#>>>
#>>> print(pm1)
#(August) 6.34
#>>>        