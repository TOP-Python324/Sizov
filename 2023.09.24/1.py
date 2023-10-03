
class Point:
    """
    Класс описывающий двумерную точку
    """

    def __init__(self, x: float, y: float):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float) -> None:
        raise TypeError(f"'{self.__class__.__name__}' object does not support coordinate assignment")

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float) -> None:
        raise TypeError(f"'{self.__class__.__name__}' object does not support coordinate assignment")

    def __repr__(self):
        return f'({self.__x}, {self.__y})'
#        return f'<{self.__x}, {self.__y}>!r'

    def __str__(self):
        return self.__repr__()
    

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__x == other.__x and self.__y == other.__y
        else:
            raise TypeError('')



# >>> p1 = Point(0, 3)
# >>> p2 = Point(4, 0)
# >>> p3 = Point(8, 3)
# >>> p1
# (0.0, 3.0)
# >>> repr(p1) == str(p1)
# True
# >>> p1 == Point(0, 3)
# True
# >>> p1.x, p1.y
# (0.0, 3.0)
# >>> p2.y = 5
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "E:\!Обучение\top\!Python\Sizov\2023.09.24\1.py", line 25, in y
#     raise TypeError(f"'{self.__class__.__name__}' object does not support coordinate assignment")
# TypeError: 'Point' object does not support coordinate assignment
# >>>
