def repeat(function):
    """Выполняет декорируемую функцию десять раз."""
    def wrapper(*args, **kwargs):
        # ИСПОЛЬЗОВАТЬ: для невостребованной переменной цикла используют имя _
        # КОММЕНТАРИЙ: имена i, j, k традиционно используются только для индексов — не нарушайте эту традицию
        for _ in range(10):
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

# ДОБАВИТЬ везде и всегда: тесты не только по примерам, но для как можно большего количества возможных ситуаций и входных данных, например:
# >>> def returning_func(x):
# ...     return x + 10
# ...
# >>> returning_func = repeat(returning_func)
# >>> returning_func(5)
# КОММЕНТАРИЙ: здесь можно обратить внимание на то, что в итоге возвращается только последнее значение
# 15


# ИТОГ: очень хорошо — 3/3
