from pathlib import Path
from sys import path
from datetime import datetime as dt


def logger(func_obj):
    """Ведёт журнал вызовов декорируемой функции в файле."""
    
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
        # ИСПОЛЬЗОВАТЬ: компактную запись там, где это не вредит читаемости кода
        file_path = Path(path[0]) / 'data/function_calls.log'
        now = dt.now()
        with open(file_path, 'a', encoding='utf-8') as fileout:
            print(f'{now.strftime("%Y.%m.%d %H:%M:%S")} - {func_obj.__name__}({args}{", " if kwargs else ""}{kwargs}) -> {result}', file=fileout)
        return result
    
    return wrapper


# ИСПОЛЬЗОВАТЬ везде: PEP 8 рекомендует добавлять пробелы после символа # — в большинстве редакторов кода, включая Notepad++, это делает команда "Вкл./Выкл. комментарий"
# E:\!Обучение\top\!Python\Sizov\2023.06.22>python -i 5.py
# >>> def testing_function():
# ...     pass
# ...
# >>> testing_function = logger(testing_function)
# >>> testing_function()

# КОММЕНТАРИЙ: исходя из показанных тестов на текущий момент первой строчки в файле не должно быть — результаты тестов должны пояснять работу приложения, а не вводить в заблуждение
# E:\!Обучение\top\!Python\Sizov\2023.06.22>type data\function_calls.log
# 2023.08.02 17:51:56 - div_round(2, 3, digits=2) -> 0.67
# 2023.08.02 17:53:02 - testing_function() -> None

# E:\!Обучение\top\!Python\Sizov\2023.06.22>python -i 5.py
# >>> def div_round(num1, num2, *, digits=0):
# ...     return round(num1 / num2, digits)
# ...
# >>> div_round = logger(div_round)
# >>> div_round(2, 3, digits=2)
# 0.67

# КОММЕНТАРИЙ: я, конечно, могу предположить, что перед этим тестом вы вручную очистили файл, но это совсем не очевидно — снова введение в заблуждение
# E:\!Обучение\top\!Python\Sizov\2023.06.22>type data\function_calls.log
# 2023.08.02 17:56:12 - div_round(2, 3, digits=2) -> 0.67

# E:\!Обучение\top\!Python\Sizov\2023.06.22>python -i 5.py
# >>> def testing_function():
# ...     pass
# ...
# >>> testing_function = logger(testing_function)
# >>> testing_function()

# E:\!Обучение\top\!Python\Sizov\2023.06.22>type data\function_calls.log
# 2023.08.02 17:56:12 - div_round(2, 3, digits=2) -> 0.67
# 2023.08.02 17:57:08 - testing_function() -> None

# ДОБАВИТЬ: тесты с другими тестовыми функциями с различными наборами аргументов

# КОММЕНТАРИЙ: файл function_calls.log разумеется должен был быть включён в ответ


# ИТОГ: хорошо, поработать с тестами — 3/5
