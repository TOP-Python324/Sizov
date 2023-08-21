from typing import Literal


class ChessKing:
    """
    Описывает шахматную фигуру короля.
    """
#    files: dict[str, int] = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
#    ranks: dict[str, int] = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8}
    # ИСПОЛЬЗОВАТЬ: написать литерал можно всегда, а потренировать генераторные выражения и встроенные функции никогда лишним не будет
    files: dict[str, int] = {chr(c): c-96 for c in range(96, 105)}
#    files: dict[str, int] = {l: c for c, l in enumerate('abcdefgh', 1)}
#    files: dict[str, int] = dict(zip('abcdefgh', range(1, 9)))
    ranks: dict[str, int] = {str(n): n for n in range(1, 9)}

    # ИСПОЛЬЗОВАТЬ: аннотацию только двух вариантов строк для параметра color
    def __init__(self, color: Literal['white', 'black'] = 'white', square: str = None) -> None:
        self.color: str = color
        if square is None:
            if self.color == 'white':
                self.square = 'e1'
            else:
                self.square = 'e8'

    def __repr__(self):
        # ПЕРЕИМЕНОВАТЬ: имена переменных i, j, k традиционно используются только для индексов — здесь вы работаете с идентификаторами и сопоставленными им объектами
        # УДАЛИТЬ: никто не гарантирует, что переменные будут названы так, как вам необходимо — это зависит не от того, кто разрабатывает класс, а от того, кто его использует
#        for i, j in globals().items():
#            if j is self:
                # ИСПРАВИТЬ: 'WK' — это 'White King', 'BK' — соответственно, 'Black King' — мне думается, что буквы 'W' и 'B' вы можете получить из атрибута color, без обращения к именам переменных
#                return f"'{self.color[:1].upper()}K: {self.square}'"
                return f"'{self.__str__()}'"

    # ИСПРАВИТЬ: никогда не проектируйте класс зависимым от произвольных действий пользователя класса (например, именования переменных для экземпляров этого класса)
    def __str__(self):
        # ПЕРЕИМЕНОВАТЬ: имена переменных i, j, k традиционно используются только для индексов — здесь вы работаете с идентификаторами и сопоставленными им объектами
        return f'{self.color[:1].upper()}K: {self.square}'

    def is_turn_valid(self, new_square: str) -> bool:
        """Принимает на вход строку нового поля и проверяет, возможен ли для данной фигуры ход с текущего поля на новое."""
        # ИСПОЛЬЗОВАТЬ: тот случай, когда выражение уже сложновато для восприятия, и его стоит разбить, даже если переменные нигде больше не будут использованы
        delta1 = self.files[self.square[0]] - self.files[new_square[0]]
        delta2 = self.ranks[self.square[1]] - self.ranks[new_square[1]]
        # УДАЛИТЬ: логическое выражение будучи вычисленным всегда возвращает True или False — в условной конструкции нет необходимости
        return abs(delta1) <= 1 and abs(delta2) <= 1


    def turn(self, new_square: str) -> None:
        """Принимает на вход строку нового поля и выполняет ход, выбрасывает ValueError в случае невозможности выполнить ход."""
        # УДАЛИТЬ: метод is_turn_valid() мы объявляли чтобы использовать
        # КОММЕНТАРИЙ: любое повторение кода, даже с незначительными изменениями, должно порождать у вас вопрос: "что я могу сделать, чтобы этого избежать?" — функциональная и объектно-ориентированная парадигмы программирования были придуманы для того, чтобы избежать постоянного дублирования кода, присущего процедурной парадигме
#        delta1 = self.files[self.square[0]] - self.files[new_square[0]]
 #       delta2 = self.ranks[self.square[1]] - self.ranks[new_square[1]]
#        if abs(delta1) <= 1 and abs(delta2) <= 1:
        if self.is_turn_valid(new_square):
            self.square = new_square
            # УДАЛИТЬ: если нет других вариантов возврата, то в явном возврате None нет необходимости: функция, в которой нет ни одного return, всегда вернёт None
#            return None
        else:
            raise ValueError


# wk = ChessKing()
# >>> wk.color
# 'white'
# >>> wk.square
# 'e1'
# >>> wk.turn('e2')
# >>> wk
# 'WK: e2'
# >>> wk.turn('d4')
# ...
# ValueError
# >>>
# >>> bk = ChessKing('black')
# >>> print(bk)
# BK: e8


# ИТОГ: нужно лучше, доработать — 3/6

# >>> wk = ChessKing()
# >>> wk.color
# 'white'
# >>> wk.square
# 'e1'
# >>> wk.turn('e2')
# >>> wk
#' WK: e2'
# >>> wk.turn('d4')
# ...
# ValueError
# >>>
# >>> bk = ChessKing('black')
# >>> print(bk)
# BK: e8
