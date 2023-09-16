class Matrix:
    """
    Класс для работы с матрицами.
    Поддерживаемые операции:
      - поэлементное сложение
      - поэлементное вычитание
      - поэлементное умножение на число
    """
    def __init__(self, rows: int, columns: int, *args):
        self.__rows = int(rows)
        self.__columns = int(columns)
        self.elements = []
        # ПЕРЕИМЕНОВАТЬ везде: при указании индексов элемента матрицы сначала приводится индекс строки, затем индекс столбца — также как и, например, для списка списков
        for column in range(columns):
            i, j = column * rows, (column+1) * rows
            self.elements.append(list(args[i:j]))

    # геттер
    @property
    def columns(self) -> int:
        return self.__columns

    # геттер
    @property
    def rows(self) -> int:
        return self.__rows

    def __str__(self):
        out = ''
        for column in range(self.__columns):
            out += ' '.join(map(str, self.elements[column])) + '\n'
        return out

    # ДОБАВИТЬ: все методы, перегружающие операторы, обычно возвращают экземпляр текущего класса
    def __add__(self, other):
        if isinstance(other, self.__class__):
            # ДОБАВИТЬ: проверку на совпадение размерностей матриц (матрицы разных размерностей не могут быть сложены)

            # ИСПРАВИТЬ: self является изменяемым объектом, поэтому здесь происходит передача по ссылке
            result = self
            # КОММЕНТАРИЙ: проблема может быть разрешена созданием новой последовательности чисел, которая пере возвратом передаётся в конструктор матрицы
            for column in range(self.__columns):
                for line in range(self.__rows):
                    result.elements[column][line] += other.elements[column][line]
            return result
        else:
            raise TypeError('NotImplementedError')

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            for column in range(self.__columns):
                for line in range(self.__rows):
                    self.elements[column][line] -= other.elements[column][line]
            return self
        else:
            raise TypeError('NotImplementedError')

    def __mul__(self, number: int):
        # ДОБАВИТЬ: проверку класса number
        for column in range(self.__columns):
            for line in range(self.__rows):
                self.elements[column][line] *= number
        return self


# ИСПРАВИТЬ: аргументы для rows и columns неотличимы от аргументов элементов матрицы — подумайте, как изменить сигнатуру конструктора, чтобы создание объекты матрицы было однозначно читаемым
M1 = Matrix(2,2,1,2,3,4)
M2 = Matrix(2,2,5,6,7,8)


# >>> M1.columns
# 2
# >>> M1.lines
# 2
# >>> M1.lines = 2
# ...
# AttributeError: property 'lines' of 'Matrix' object has no setter
# >>>
# >>> print(M1)
# 1 2
# 3 4


# ИТОГ: неплохо, хотя можно лучше, доработайте — 8/12
