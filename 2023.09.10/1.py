class Matrix:
    """
   Класс для работы с матрицами.
   Класс поддерживает операции:
    - поэлементное сложение;
    - поэлементное вычитание;
    - поэлементное умножение на число
   """    

    def __init__(self, columns: int, lines: int, *args):
        self.__columns = int(columns)
        self.__lines = int(lines)
        self.element = []
        for column in range(columns):
            self.element.append(list(args[column*lines:(column+1)*lines]))

    # геттер
    @property
    def columns(self) -> int:
        return self.__columns

    # геттер
    @property
    def lines(self) -> int:
        return self.__lines

    def __str__(self):
        out = ''
        for column in range(self.__columns):
            out += ' '.join(map(str, self.element[column])) + '\n'
        return out


    def __add__(self, other):
        if isinstance(other, self.__class__):
            result = self
            for column in range(self.__columns):
                for line in range(self.__lines):
                    result.element[column][line] += other.element[column][line]
            return result
        else:
            raise TypeError('NotImplementedError')


    def __sub__(self, other):
        if isinstance(other, self.__class__):
            for column in range(self.__columns):
                for line in range(self.__lines):
                    self.element[column][line] -= other.element[column][line]
            return self
        else:
            raise TypeError('NotImplementedError')


    def __mul__(self, number: int):
        for column in range(self.__columns):
            for line in range(self.__lines):
                self.element[column][line] *= number
        return self

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