def taxi_cost(length: int, waiting_time: int = 0) -> int | None:
    """Вычисляет стоимость поездки на такси"""
    if length < 0 or waiting_time < 0:
        return None
    price = 80
    if length == 0:
        # ИСПРАВИТЬ: вычисление waiting_time*3 прописано несколько раз — самоповторов обычно лучше избегать — если эту часть выражения убрать из этой строчки...
        price += 80 + waiting_time*3
    # ИСПРАВИТЬ: ...то заголовок блока else можно убрать, а отступ инструкций из этого блока уменьшить на один уровень — тогда они будут вычисляться вне зависимости от условия length == 0
    else:
        price += length / 150 * 6
        price += waiting_time * 3
    # ИСПРАВИТЬ:
    return int(round(price, 0))
    # ИСПОЛЬЗОВАТЬ: а ещё можно всё то же самое написать в одну строчку:
    # return round(80 + (80, 0)[length] + length/150*6 + waiting_time*3)


# >>> taxi_cost(2000)
# 160
# >>> taxi_cost(0, 10)
# 190
# >>> taxi_cost(42130, 8)
# 1789
# >>> print(taxi_cost(-10))
# None


# ИТОГ: хорошо, но можно лучше — 2/3
