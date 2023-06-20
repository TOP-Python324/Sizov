def math_function_resolver(math_function: 'function', *numbers: tuple[int|float], strings: bool = False) -> list[float | str]:
    """Вычисляет округлённые значения для различных математических функций.
    Математическая функция должна принимать один обязательный позиционно-ключевой аргумент — число x, для которого необходимо вычислить значение математической функции.
    """
    result = []
    for number in numbers:
        result += [round(math_function(number), 2)]
    
    if strings:
        result = list(map(str, result))
        
    return result    
    
# >>> math_function_resolver(lambda x: 0.5*x + 2, *range(1, 10))
# [2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5]
# >>> math_function_resolver(lambda x: -0.5*x + 2, *range(1, 10))
# [1.5, 1.0, 0.5, 0.0, -0.5, -1.0, -1.5, -2.0, -2.5]
# >>> math_function_resolver(lambda x: 2.72**x, *range(1, 10), strings=True)
# ['2.72', '7.4', '20.12', '54.74', '148.88', '404.96', '1101.49', '2996.07', '8149.3']