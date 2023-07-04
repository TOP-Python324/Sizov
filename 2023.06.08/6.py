def orth_triangle(*, cathetus1: int = 0, cathetus2: int = 0, hypotenuse: int = 0) -> float:
    """Вычисляет третью сторону прямоугольного треугольника по двум переданным"""
    # передали два катета
    if hypotenuse == 0 and cathetus1 != 0 and cathetus2 != 0:
        side = pow(cathetus1**2 + cathetus2**2, 0.5)
    # если нет первого катета
    elif cathetus1 == 0 and cathetus2 != 0 and hypotenuse > cathetus2:
        side = pow(hypotenuse**2 - cathetus2**2, 0.5)
    # если нет второго катета
    elif cathetus2 == 0 and cathetus1 != 0 and hypotenuse > cathetus1:
        side = pow(hypotenuse**2 - cathetus1**2, 0.5)
    # вычисление невозможно
    else:
        side = None
        
    return side


# >>> orth_triangle(cathetus1=3, hypotenuse=5)
# 4.0
# >>> orth_triangle(cathetus1=8, cathetus2=15)
# 17.0
# >>> print(orth_triangle(cathetus2=9, hypotenuse=3))
# None

# ДОБАВИТЬ везде и всегда: тесты не только по примерам, но для всех возможных ситуаций, например:
# >>> print(orth_triangle(cathetus1=10))
# None
# >>> print(orth_triangle(cathetus1=3, cathetus2=4, hypotenuse=5))
# None


# ИТОГ: отлично — 4/4
