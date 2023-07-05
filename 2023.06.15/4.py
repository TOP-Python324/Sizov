def repeat(function):
    """Выполняет декорируемую функцию десять раз."""
    def wrapper(*args, **kwargs):
        # ИСПОЛЬЗОВАТЬ: для невостребованной переменной цикла используют имя _
        # КОММЕНТАРИЙ: имена i, j, k традиционно используются только для индексов
        for i in range(10):
            result = function(*args, **kwargs)
        return result

    return wrapper   


# >>> def testing_function():
# ...     print('python')
# ...
# >>> testing_function = repeat(testing_function)
# >>>
# >>> testing_function()
# python
# python
# python
# python
# python
# python
# python
# python
# python
# python

