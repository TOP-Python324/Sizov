def logger(function):
    """Ведёт журнал вызовов декорируемой функции в стандартном потоке вывода ."""
    def wrapper(*args, **kwargs):
        result = None
        # формируем журнал функции
        # ИСПОЛЬЗОВАТЬ: согласно PEP 8, комментарий следует располагать над комментируемой строчкой кода
        # добавляем название функции и (
        out = function.__name__ + '('
        # добавляем позиционные аргументы переданные в функцию
        for arg in args:
            out += str(arg) + ', '
        # если передали значений для позиционных аргументов меньше чем есть у функции то дописываем значениями по умолчанию
        if len(args) < function.__code__.co_argcount:
            # вычисляем сколько значений нужно дописать
            count = function.__code__.co_argcount - len(args)
            # переводим значения по умолчанию в список
            list_arg = list(function.__defaults__)
            while count > 0:
                out += str(list_arg[len(args)-count-1]) + ', '
                count -= 1
        # добавляем ключевые аргументы
        for key, val in kwargs.items():
            out += key + '=' + str(val)
        # добавляем ключевые аргументы со значениями по умолчанию если они не переданы
        if function.__kwdefaults__ != None:
            for key, val in function.__kwdefaults__.items():
                if not (key in kwargs.keys()):
                    out += key + '=' + str(val) 
        out += ') -> '

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

