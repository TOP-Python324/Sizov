class Point:
    """
    Класс описывающий двумерную точку
    """

    def __init__(self, x: float = 0, y: float = 0):
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

    def __str__(self):
        return self.__repr__()


    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__x == other.__x and self.__y == other.__y
        else:
            raise TypeError('')


class Line:
    """
    Класс описывающий отрезок
    """

    def __init__(self, start_point: Point, end_point: Point):
        self.__start = start_point
        self.__end = end_point
#        self.__length = ((end_point.x - start_point.x)**2 + (end_point.y - start_point.y)**2)**0.5
        self.__length = self.__length_calc(start_point, end_point)

    @staticmethod
    def __length_calc(point1: Point, point2: Point) -> float:
        """Вычисляет расстояние между двумя точками."""
        delta_x = point2.x - point1.x 
        delta_y = point2.y - point1.y 
        return (delta_x**2 + delta_y**2)**0.5


    @property
    def start(self) -> Point:
        return self.__start

    @property
    def end(self) -> Point:
        return self.__end

    @property
    def length(self) -> float:
        return self.__length

    @start.setter
    def start(self, new_point):
        if isinstance(new_point, self.start.__class__):
            self.__start._Point__x = new_point.x
            self.__start._Point__y = new_point.y
            self.__length = self.__length_calc(self.start, self.end)
        else:
            raise TypeError(f"'start' attribute of '{self.__class__.__name__}' object supports only '{self.start.__class__.__name__}' object assignment")

    @end.setter
    def end(self, new_point):
        if isinstance(new_point, self.end.__class__):
            self.__end._Point__x = new_point.x
            self.__end._Point__y = new_point.y
            self.__length = self.__length_calc(self.start, self.end)
        else:
            raise TypeError(f"'end' attribute of '{self.__class__.__name__}' object supports only '{self.end.__class__.__name__}' object assignment")

    @length.setter
    def length(self, new_length: float) -> None:
        raise TypeError(f"'{self.__class__.__name__}' object does not support length assignment")

    def __repr__(self):
        return f'({self.__start.x}, {self.__start.y})———({self.__end.x}, {self.__end.y})'

    def __str__(self):
        return self.__repr__()


class Polygon(list):
    """
    Класс описывающий многоугольник
    """

    def __init__(self, side1: Line, side2: Line, side3: Line, *sides: Line):
        super().__init__([side1, side2, side3])
        for side in sides:
            super().append(side)

    def _is_closed(self) -> bool:
        """Проверяет, формируют ли отрезки замкнутый многоугольник."""
        for i in range(len(self)-1):
            if self[i].end.x != self[i+1].start.x or self[i].end.y != self[i+1].start.y:
                return False
        if self[-1].end.x != self[0].start.x or self[-1].end.y != self[0].start.y:
            return False
        return True

    @property
    def perimeter(self) -> float:
        """Вычисляет периметр многоугольника."""
        if self._is_closed():
            perimeter = 0
            for side in self:
                perimeter += side.length
            return perimeter
        else:
            raise ValueError("line items doesn't form a closed polygon")



# >>> p1 = Point(0, 3)
# >>> p2 = Point(4, 0)
# >>> p3 = Point(8, 3)
# >>> p1
# (0.0, 3.0)
# >>> repr(p1) == str(p1)
# True
# >>> p1 == Point(0, 3)
# True
# >>> p2 == Point(0, 3)
# False
# >>> p1.x, p1.y
# (0.0, 3.0)
# >>> p2.y = 5
# ...
# TypeError: 'Point' object does not support coordinate assignment
# >>>
# >>> l1 = Line(p1, p2)
# >>> l1
# (0.0, 3.0)———(4.0, 0.0)
# >>> l2 = Line(p2, p3)
# >>> l3 = Line(p3, p1)
# >>> repr(l1) == str(l1)
# True
# >>> l1.length
# 5.0
# >>> l1.length = 10
# ...
# TypeError: 'Line' object does not support length assignment
# >>> l3.start = 12
# ...
# TypeError: 'start' attribute of 'Line' object supports only 'Point' object assignment
# >>> l1.end = p3
# >>> l1
# (0.0, 3.0)———(8.0, 3.0)
# >>> l1.length
# 8.0
# >>>
# >>> Polygon(l1,l2,l3)
# [(0.0, 3.0)———(4.0, 0.0), (4.0, 0.0)———(8.0, 3.0), (8.0, 3.0)———(0.0, 3.0)]
# >>> pol1=Polygon(l1,l2,l3)
# >>> pol1.perimeter
# 18.0
# >>>
# >>> pol1.perimeter = 20
# ...
# AttributeError: property 'perimeter' of 'Polygon' object has no setter
# >>>