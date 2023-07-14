from collections.abc import Iterable


def product(numbers: Iterable[float]) -> float:
    """Возвращает произведение чисел."""
    result = numbers[0]
    if len(numbers) > 1:
        result *= product(numbers[1:])
    return float(result)


# >>> product(range(10, 60, 10))
# 12000000.0
# >>> product((0.12, 0.05, -0.09, 0.0, 0.21))
# -0.0
# >>>

