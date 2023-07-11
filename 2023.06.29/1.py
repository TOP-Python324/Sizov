from collections.abc import Iterable

def product(numbers: Iterable[float]) -> float:
    """Возвращает произведение чисел."""
    result = 1.0
    
    for elem in numbers:
        if isinstance(elem, Iterable):
            result *= product(elem)
        else:
            result *= elem
    
    return result



# >>> product(range(10, 60, 10))
# 12000000.0
# >>> product((0.12, 0.05, -0.09, 0.0, 0.21))
# -0.0
# >>> product((0.2, 5, 0.1,(1 , 10)))
# 1.0
# >>>