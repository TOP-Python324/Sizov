def int_base(number: str, in_base: int, out_base: int) -> str:
    """Преобразовывает число из произвольной системы счисления в произвольную"""
    # если не правильно указали системы счисления
    if in_base > 36 or out_base > 36:
        # ИСПОЛЬЗОВАТЬ: круглые скобки используются для формирования кортежа, генераторного выражения, изменения приоритетов операторов и записи многострочных выражений — больше нигде и никак
        return None
    result = base_dec(number, in_base)
    # если преобразование невозможно
    if result == None:
        return None
    result = dec_base(result, out_base)
    return result


def base_dec(number: str, base: int) -> int:
    """Преобразовывает число из произвольной системы счисления в десятичную"""
    result = 0
    # переворачиваем для удобства
    number = number[::-1]
    pos = 0
    for n in number:
        # проверка на символы цифр
        if 48 <= ord(n) <= 57:
            result += int(n) * base**pos
        # проверка на латинские буквенные символы в верхнем регистре
        elif 65 <= ord(n) <= 90:
            result += (ord(n)-55) * base**pos
        # проверка на латинские буквенные символы в нижнем регистре
        elif 97 <= ord(n) <= 122:
            result += (ord(n)-87) * base**pos
        else:
            return None
        pos += 1
    return result


def dec_base(number: int, base: int) -> str:
    """Преобразовывает число из десятичной системы счисления в произвольную"""
    result = ''
    while number // base > base:
        if number % base < 10:
            result += str(number%base)
        else:
            result += chr(87 + number%base)
        number //= base
       
    if number % base < 10:
        result += str(number%base)
    else:
        result += chr(87 + number%base)
       
    if number // base < 10:
        result += str(number//base)
    else:
        result += chr(87 + number//base)
       
    return result[::-1]


# >>> int_base('ff00', 16, 2)
# '1111111100000000'
# >>> int_base('1101010', 2, 30)
# '3g'

