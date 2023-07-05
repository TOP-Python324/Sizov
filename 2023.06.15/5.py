def logger(function):
    """Ведёт журнал вызовов декорируемой функции в стандартном потоке вывода ."""
    def wrapper(*args, **kwargs):
        result = None
        # формируем журнал функции
        # ИСПОЛЬЗОВАТЬ: согласно PEP 8, комментарий следует располагать над комментируемой строчкой кода
        # добавляем название функции и (
        out = function.__name__ + '('
        # добавляем позиционные аргументы переданные в функцию
        # ИСПОЛЬЗОВАТЬ: есть замечательный строковый метод join() — его использование позволит избежать появления в выводе лишних знаков препинания (см. тест ниже)
        # for arg in args:
            # out += str(arg) + ', '
        out += ', '.join(map(str, args))
        # если передали значений для позиционных аргументов меньше чем есть у функции то дописываем значениями по умолчанию
        if len(args) < function.__code__.co_argcount:
            # вычисляем сколько значений нужно дописать
            count = function.__code__.co_argcount - len(args)
            # переводим значения по умолчанию в список
            # УДАЛИТЬ: зачем? в этом нет никакой необходимости, кортежи являются точно такими же индексируемыми последовательностями как и списки
            list_arg = list(function.__defaults__)
            while count > 0:
                out += str(list_arg[len(args)-count-1]) + ', '
                count -= 1
        # добавляем ключевые аргументы
        for key, val in kwargs.items():
            # ИСПОЛЬЗОВАТЬ: f-строки
            # out += key + '=' + str(val)
            out += f'{key}={val}'
        # добавляем ключевые аргументы со значениями по умолчанию если они не переданы
        # ИСПРАВИТЬ: None — это уникальный объект, он не копируется в памяти, при необходимости возвращается ссылка на один и тот же объект — поэтому проверку ниже лучше осуществить с помощью оператора is not
        if function.__kwdefaults__ != None:
            for key, val in function.__kwdefaults__.items():
                if not (key in kwargs.keys()):
                    # ИСПРАВИТЬ: f-строки — это мощный и очень производительный инструмент, используйте их всякий раз, когда вам необходима конкатенация строковых представлений не строковых объектов
                    out += key + '=' + str(val) 
        out += ') -> '

        try:
            result = function(*args, **kwargs)
            print(f'{out}{result}')
        except Exception as exception:
            print(f'{out}\n\t{exception.__class__.__name__}: {exception}')
        return result

    return wrapper


# >>> def div_round(num1, num2, *, digits=0):
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

# ДОБАВИТЬ везде и всегда: тесты не только по примерам, но для как можно большего количества возможных ситуаций и входных данных, например:

# >>> def adder(a, b):
# ...     return a + b
# ...
# >>> adder = logger(adder)
# >>> adder(5, 2)
# adder(5, 2, ) -> 7
# 7

# >>> def adder(*, n1=0, n2=0):
# ...     return n1 + n2
# ...
# >>> adder = logger(adder)
# >>>
# >>> adder(n2=3)
# adder(n2=3n1=0) -> 3
# 3


# ИТОГ: хорошо, но базовые типы необходимо изучить лучше — 4/6


# СДЕЛАТЬ: изучите более оптимальный вариант реализации:
def logger(func_obj):
    if func_obj.__defaults__ is None:
        func_obj.__defaults__ = ()
    if func_obj.__kwdefaults__ is None:
        func_obj.__kwdefaults__ = {}

    def wrapper(*args, **kwargs):
        try:
            result = func_obj(*args, **kwargs)
        except Exception as exc:
            result = f'\n    {exc.__class__.__name__}: {exc}'

        i = len(args) - func_obj.__code__.co_argcount
        args = ', '.join(
            str(arg)
            for arg in args + (func_obj.__defaults__[i:] if i else ())
        )
        kwargs = ', '.join(
            f'{key}={val}'
            for key, val in (func_obj.__kwdefaults__ | kwargs).items()
        )
        print(f'{func_obj.__name__}({args}{", " if kwargs else ""}{kwargs}) -> {result}')
        return result

    return wrapper
