# ДОБАВИТЬ: None в аннотацию типа возвращаемого значения
def int_base(number: str, in_base: int, out_base: int) -> str:
    """Преобразовывает число из произвольной системы счисления в произвольную"""
    # если не правильно указали системы счисления
    # ИСПРАВИТЬ: не проверена нижняя граница диапазона значений для систем счисления
    if in_base > 36 or out_base > 36:
        # ИСПОЛЬЗОВАТЬ: круглые скобки используются для формирования кортежа, генераторного выражения, изменения приоритетов операторов и записи многострочных выражений — больше нигде и никак
        return None
    result = base_dec(number, in_base)
    # если преобразование невозможно
    # ИСПРАВИТЬ: None — это уникальный объект, он не копируется в памяти, при необходимости возвращается ссылка на один и тот же объект — поэтому такая проверка осуществляется с помощью оператора is
    if result == None:
        return None
    result = dec_base(result, out_base)
    return result


# ДОБАВИТЬ: None в аннотацию типа возвращаемого значения
def base_dec(number: str, base: int) -> int:
    """Преобразовывает число из произвольной системы счисления в десятичную"""
    result = 0
    # переворачиваем для удобства
    number = number[::-1]
    pos = 0
    for n in number:
        # КОММЕНТАРИЙ: такие проверки на каждой итерации не добавляют производительности — имеет смысл заранее вычислить соответствие каждого символа числу в десятичной системе счисления
        # проверка на символы цифр
        if 48 <= ord(n) <= 57:
            result += int(n) * base**pos
        # проверка на латинские буквенные символы в верхнем регистре
        elif 65 <= ord(n) <= 90:
            result += (ord(n) - 55) * base**pos
        # проверка на латинские буквенные символы в нижнем регистре
        elif 97 <= ord(n) <= 122:
            result += (ord(n) - 87) * base**pos
        else:
            return None
        pos += 1
    return result


def dec_base(number: int, base: int) -> str:
    """Преобразовывает число из десятичной системы счисления в произвольную"""
    result = ''
    while number // base > base:
        # ИСПОЛЬЗОВАТЬ: всегда внимательно следите за величиной отступа (особенно, когда копируете откуда-то код)
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

# ДОБАВИТЬ везде и всегда: тесты не только по примерам, но для всех возможных ситуаций, например:
# >>> print(int_base('abc', 10, 2))
# КОММЕНТАРИЙ: а должно быть None
# 2001100010


# ИТОГ: неплохо, но можно лучше — 4/7


# ИСПОЛЬЗОВАТЬ: изучите более оптимальный вариант реализации:
numbers_digits = dict(zip(range(36), '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
digits_numbers = {v: k for k, v in numbers_digits.items()}

def to_decimal(number: str, base: int) -> int | None:
    return sum(
        base**rank * digits_numbers[digit.upper()]
        for rank, digit in enumerate(number[::-1])
    )

def from_decimal(number: int, base: int) -> str:
    result = ''
    while number:
        number, remainder = divmod(number, base)
        result += numbers_digits[remainder]
    return result[::-1]

def int_base(number: str, base_from: int, base_to: int) -> str | None:
    if not (
            number
        and 2 <= base_from <= 36
        and 2 <= base_to <= 36
        and digits_numbers[max(number).upper()] < base_from
    ):
        return None

    number = to_decimal(number, base_from) if base_from != 10 else int(number)
    return from_decimal(number, base_to)

