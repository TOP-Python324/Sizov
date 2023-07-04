def numbers_strip(numbers: list[float], n: int = 1, *, copy: bool = False) -> list[float]:
    """Удаляет n минимальных и n максимальных чисел из списка"""
    # если вернуть копию
    if copy:
        # ПЕРЕИМЕНОВАТЬ: в создании новой переменной нет необходимости — используйте имя numbers...
        numbers_new = numbers.copy()
    # УДАЛИТЬ: ... и тогда блок else не понадобится
    else:
        numbers_new = numbers
    # ИСПОЛЬЗОВАТЬ: для невостребованной переменной цикла используют имя _
    for _ in range(n):
        numbers_new.remove(min(numbers_new))
        numbers_new.remove(max(numbers_new))
    return numbers_new


# >>> sample = [1, 2, 3, 4]
# >>> sample_stripped = numbers_strip(sample)
# >>> sample_stripped
# [2, 3]
# >>> sample is sample_stripped
# True

# >>> sample = [10, 20, 30, 40, 50]
# >>> sample_stripped = numbers_strip(sample, 2, copy=True)
# >>> sample_stripped
# [30]
# >>> sample is sample_stripped
# False

# ДОБАВИТЬ везде и всегда: тесты не только по примерам, но для всех возможных ситуаций, например:
# >>> sample_stripped = numbers_strip([])
# ...
# ValueError: min() arg is an empty sequence


# ИТОГ: очень хорошо — 3/4
