class Tetrahedron:
    """
    Класс описывает правильный тетраэдр.
    ...
    Атрибуты
    --------
    edge : float
        длина ребра
    Методы
    ------
    surface(): -> float
        Вычисляет площадь поверхности.
    volume(): -> float
        Вычисляет объём тела.
    """
    
    # конструктор
    def __init__(self, edge: float) -> None:
        # атрибуты экземпляра
        self.edge: float = float(edge)
        
    def surface(self) -> float:
        """ Вычисляет площадь поверхности"""
        return self.edge**2 * 3**0.5
        
    def volume(self) -> float:
        """ Вычисляет объём тела"""
        return self.edge**3 * 2**0.5 / 12

#>>> t1 = Tetrahedron(5)
#>>> t1.edge
#5.0
#>>> t1.surface()
#43.30127018922193
#>>> t1.volume()
#14.73139127471974
#>>>
#>>> t1.edge = 6
#>>> t1.surface()
#62.35382907247958
