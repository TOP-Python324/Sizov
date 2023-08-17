class ChessKing:
    """
    Описывает шахматную фигуру короля.
    """
    files: dict[str, int] = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
    ranks: dict[str, int] = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8}
    
    def __init__(self, color: str = 'white', square: str = None) -> None:
        self.color: str = color
        if square is None:
            if self.color == 'white':
                self.square = 'e1'
            else:    
                self.square = 'e8'
        
    def __repr__(self):
        # ПЕРЕИМЕНОВАТЬ: имена переменных i, j, k традиционно используются только для индексов — здесь вы работаете с идентификаторами и сопоставленными им объектами
        for i, j in globals().items():
            if j is self:
                return f"'{i.upper()}: {self.square}'"
    
    def __str__(self):
        # ПЕРЕИМЕНОВАТЬ: имена переменных i, j, k традиционно используются только для индексов — здесь вы работаете с идентификаторами и сопоставленными им объектами
        for i, j in globals().items():
            if j is self:
                return f'{i.upper()}: {self.square}'
        
    def is_turn_valid(self, new_square: str) -> bool:    
        """Принимает на вход строку нового поля и проверяет, возможен ли для данной фигуры ход с текущего поля на новое."""
        # ИСПОЛЬЗОВАТЬ: тот случай, когда выражение уже сложновато для восприятия, и его стоит разбить, даже если переменные нигде больше не будут использованы
        delta1 = self.files[self.square[0]] - self.files[new_square[0]]
        delta2 = self.ranks[self.square[1]] - self.ranks[new_square[1]]
        if abs(delta1) <= 1 and abs(delta2) <= 1:
            return True
        else:
            return False

    def turn(self, new_square: str) -> None:    
        """Принимает на вход строку нового поля и выполняет ход, выбрасывает ValueError в случае невозможности выполнить ход."""
        delta1 = self.files[self.square[0]] - self.files[new_square[0]]
        delta2 = self.ranks[self.square[1]] - self.ranks[new_square[1]]
        if abs(delta1) <= 1 and abs(delta2) <= 1:
            self.square = new_square
            return None
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
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "E:\!Обучение\top\!Python\Sizov\2023.08.10\3.py", line 40, in turn
#    raise ValueError
#    ^^^^^^^^^^^^^^^^
# ValueError
# >>>
# >>> bk = ChessKing('black')
# >>> print(bk)
# BK: e8

