from collections.abc import Iterable

class Matrix:
    """
    Класс для работы с матрицами.
    Поддерживаемые операции:
      - поэлементное сложение
      - поэлементное вычитание
      - поэлементное умножение на число
    """

    def __init__(self, numbers: Iterable[int], *, rows: int, columns: int):
        self.__rows = int(rows)
        self.__columns = int(columns)
        self.elements = []
        # ПЕРЕИМЕНОВАТЬ везде: при указании индексов элемента матрицы сначала приводится индекс строки, затем индекс столбца — также как и, например, для списка списков
        for row in range(rows):
            i, j = row * columns, (row+1) * columns
            self.elements.append(list(numbers[i:j]))

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
        for row in range(self.__rows):
            out += ' '.join(map(str, self.elements[row])) + '\n'
        return out

    # ДОБАВИТЬ: все методы, перегружающие операторы, обычно возвращают экземпляр текущего класса
    def __add__(self, other):
        if isinstance(other, self.__class__):
            # ДОБАВИТЬ: проверку на совпадение размерностей матриц (матрицы разных размерностей не могут быть сложены)
            if self.__rows == other.__rows and self.__columns == other.__columns:
                # ИСПРАВИТЬ: self является изменяемым объектом, поэтому здесь происходит передача по ссылке
                result = []
                # КОММЕНТАРИЙ: проблема может быть разрешена созданием новой последовательности чисел, которая пере возвратом передаётся в конструктор матрицы
                for row in range(self.__rows):
                    for column in range(self.__columns):
                        result.append(self.elements[row][column] + other.elements[row][column])
                return self.__class__(result, rows = self.__rows, columns = self.__columns)
            else:
                raise TypeError('Матрицы должны быть одного размера')
        else:
            raise TypeError('NotImplementedError')

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            if self.__rows == other.__rows and self.__columns == other.__columns:
                result = []
                for row in range(self.__rows):
                    for column in range(self.__columns):
                        result.append(self.elements[row][column] - other.elements[row][column])
                return self.__class__(result, rows = self.__rows, columns = self.__columns)
            else:
                raise TypeError('Матрицы должны быть одного размера')
        else:
            raise TypeError('NotImplementedError')

    def __mul__(self, number: int):
        # ДОБАВИТЬ: проверку класса number
        if isinstance(number, int):
            result = []
            for column in range(self.__columns):
                for line in range(self.__rows):
                    result.append(self.elements[column][line] * number)
            return self.__class__(result, rows = self.__rows, columns = self.__columns)
        else:
            raise TypeError('NotImplementedError')


# ИСПРАВИТЬ: аргументы для rows и columns неотличимы от аргументов элементов матрицы — подумайте, как изменить сигнатуру конструктора, чтобы создание объекты матрицы было однозначно читаемым
# M1 = Matrix(2,2,1,2,3,4)
# M2 = Matrix(2,2,5,6,7,8)


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

# >>> M1=Matrix([1,2,3,4],rows=2,columns=2)
# >>> M2=Matrix([2,3,4,5],rows=2,columns=2)
# >>> M = M1+M2
# >>> print(M)
# 3 5
# 7 9
# 
# >>> M3=Matrix([1,2,3,4,5,6],rows=2,columns=3)
# >>> M=M1+M3
# ...
#     raise TypeError('Матрицы должны быть одного размера')
# TypeError: Матрицы должны быть одного размера
# >>> M = M2 - M1
# >>> print(M)
# 1 1
# 1 1
# 
# >>> print(M1)
# 1 2
# 3 4
# >>>
# >>> print(M1*2)
# 2 4
# 6 8
# 
# >>> print(M1)
# 1 2
# 3 4
