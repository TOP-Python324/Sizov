def taxi_cost(length: int, waiting_time: int = 0) -> int | None:
    """Вычисляет стоимость поездки на такси"""
    if length < 0 or waiting_time < 0:
        return None
    price = 80
    if length == 0:
        price += 80 + waiting_time*3
    else:
        price += length / 150 * 6
        price += waiting_time * 3
    return int(round(price,0))    


# >>> taxi_cost(2000)
# 160
# >>> taxi_cost(0, 10)
# 190
# >>> taxi_cost(42130, 8)
# 1789
# >>> print(taxi_cost(-10))
# None

