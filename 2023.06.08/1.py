def strong_password(password: str) -> bool:
    """Проверяет является ли пароль надёжным"""
    # ИСПОЛЬЗОВАТЬ: согласно PEP 8, комментарий следует располагать над комментируемой строчкой кода
    # если длина меньше 8 то сразу выходим
    if len(password) < 8:
        return False
    
    flag_digit = False
    count_digit = 0
    flag_alpha = False
    flag_ALPHA = False
    flag_symbol = False

    # ПЕРЕИМЕНОВАТЬ: символ — character, char, ch
    for s in password:
        # проверка на латинские буквенные символы в верхнем регистре
        if 65 <= ord(s) <= 90:
            flag_ALPHA = True
        # проверка на латинские буквенные символы в нижнем регистре
        elif 97 <= ord(s) <= 122:
            flag_alpha = True
        # проверка на символы цифр
        elif 48 <= ord(s) <= 57:
            count_digit += 1
            if count_digit >= 2:
                flag_digit = True
        # проверка на спецсимволы
        elif (32 <= ord(s) <= 47) or (91 <= ord(s) <= 96) or (123 <= ord(s) <= 126):
            flag_symbol = True
    
    if flag_ALPHA and flag_alpha and flag_digit and flag_symbol:
        return True
    else:
        return False


# strong_password('asdER_12(sad^')
# True
# strong_password('12345678')
# False


# КОММЕНТАРИЙ: PEP 8 — сборник рекомендаций по стилистическому оформлению Python кода — их стоит использовать для большего удобства чтения своего и чужого кода: https://peps.python.org/pep-0008/

