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
        
        script_dir = Path(path[0])
        file_path = script_dir / 'data/function_calls.log'
        now = dt.now()

        with open(file_path, 'a', encoding='utf-8') as fileout:
            print(f'{now.strftime("%Y.%m.%d %H:%M:%S")} - {func_obj.__name__}({args}{", " if kwargs else ""}{kwargs}) -> {result}', file=fileout)
        return result
    
    return wrapper
    
#E:\!Обучение\top\!Python\Sizov\2023.06.22>python -i 5.py
#>>> def testing_function():
#...     pass
#...
#>>> testing_function = logger(testing_function)
#>>> testing_function()
#>>> ^Z


#E:\!Обучение\top\!Python\Sizov\2023.06.22>type data\function_calls.log

#2023.08.02 17:51:56 - div_round(2, 3, digits=2) -> 0.67
#2023.08.02 17:53:02 - testing_function() -> None

#E:\!Обучение\top\!Python\Sizov\2023.06.22>python -i 5.py
#>>> def div_round(num1, num2, *, digits=0):
#...     return round(num1 / num2, digits)
#...
#>>> div_round = logger(div_round)
#>>> div_round(2, 3, digits=2)
#0.67
#>>> ^Z


#E:\!Обучение\top\!Python\Sizov\2023.06.22>type data\function_calls.log
#2023.08.02 17:56:12 - div_round(2, 3, digits=2) -> 0.67

#E:\!Обучение\top\!Python\Sizov\2023.06.22>python -i 5.py
#>>> def testing_function():
#...     pass
#...
#>>> testing_function = logger(testing_function)
#>>> testing_function()
#>>> ^Z


#E:\!Обучение\top\!Python\Sizov\2023.06.22>type data\function_calls.log
#2023.08.02 17:56:12 - div_round(2, 3, digits=2) -> 0.67
#2023.08.02 17:57:08 - testing_function() -> None
  