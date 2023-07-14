from collections.abc import Iterable


def product(numbers: Iterable[float]) -> float:
    """Возвращает произведение чисел."""
    # ИСПРАВИТЬ: есть небольшая проблемка — см. тест ниже
    result = 1 if len(numbers) == 0 else numbers[0]
    if len(numbers) > 1: #1
        # КОММЕНТАРИЙ: да, именно так
        result *= product(numbers[1:])
   
    return float(result)


# >>> product(range(10, 60, 10))
# 12000000.0
# >>> product((0.12, 0.05, -0.09, 0.0, 0.21))
# -0.0
# >>>
# КОММЕНТАРИЙ: а ведь я вам уже говорил, что свой код надо тестировать не только примерами из задания
# >>> product([])
# КОММЕНТАРИЙ: должно быть 1.0 — по аналогии со встроенной функцией sum()
# ...
# IndexError: list index out of range


# ИТОГ: уже лучше, но всё ещё нужна доработка — 3/4
