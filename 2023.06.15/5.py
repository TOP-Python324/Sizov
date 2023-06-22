def logger(function):
    """Ведёт журнал вызовов декорируемой функции в стандартном потоке вывода ."""
    
    def wrapper(*args, **kwargs):
        result = None
        
        # формируем журнал функции
        out = function.__name__ + '(' # добавляем название функции и (
        
        for arg in args: # добавляем позиционные аргументы переданные в функцию
                out += str(arg) + ', ' 
        
        if len(args) < function.__code__.co_argcount: # если передали значений для позиционных аргументов меньше чем есть у функции то дописываем значениями по умолчанию
            count = function.__code__.co_argcount - len(args) # вычисляем сколько значений нужно дописать
            list_arg = list(function.__defaults__) # переводим значения по умолчанию в список
            while count > 0:
                out += str(list_arg[len(args) - count -1]) + ', '
                count -= 1

        
        for key, val in kwargs.items(): # добавляем ключевые аргументы
                out += key + '=' + str(val) 
                
        if function.__kwdefaults__ != None: # добавляем ключевые аргументы со значениями по умолчанию если они не переданы     
            for key, val in function.__kwdefaults__.items():
                if not (key in kwargs.keys()):
                    out += key + '=' + str(val) 
        out +=') -> '
            
            
        try:
            result = function(*args, **kwargs) 
            print(f'{out}{result}')    


        except Exception as exception:
            print(f'{out}\n\t{exception.__class__.__name__}: {exception}')

            
        return result            
        
    
    return wrapper
    
# def div_round(num1, num2, *, digits=0):
# ...     return round(num1 / num2, digits)
# ...
# >>> div_round = logger(div_round)
# >>>
# >>> div_round(1, 3, digits=2)
# div_round(1, 3, digits=2) -> 0.33
# 0.33
# >>> div_round(7, 2)
# div_round(7, 2, digits=0) -> 4.0
# 4.0
# >>> div_round(5, 0)
# div_round(5, 0, digits=0) ->
#         ZeroDivisionError: division by zero
# >>>
# >>> def div_round(num1, num2=1, *, digits=0):
# ...     return round(num1 / num2, digits)
# ...
# >>> div_round = logger(div_round)
# >>>
# >>> div_round(1, 3, digits=2)
# div_round(1, 3, digits=2) -> 0.33
# 0.33
# >>> div_round(7)
# div_round(7, 1, digits=0) -> 7.0
# 7.0
