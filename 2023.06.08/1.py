def strong_password(password: str) -> bool:
    """Проверяет является ли пароль надёжным"""
    
    if len(password) < 8: # если длина меньше 8 то сразу выходим
        return False
    
    flag_digit = False
    count_digit = 0
    flag_alpha = False
    flag_ALPHA = False
    flag_symbol = False
    
    for s in password: 
        if 65 <= ord(s) <= 90: # проверка на латинские буквенные символы в верхнем регистре
            flag_ALPHA = True  

        elif 97 <= ord(s) <= 122: # проверка на латинские буквенные символы в нижнем регистре
            flag_alpha = True

        elif 48 <= ord(s) <= 57: # проверка на символы цифр
            count_digit += 1
            if count_digit >= 2:
                flag_digit = True
                
        elif (32 <= ord(s) <= 47) or (91 <= ord(s) <= 96) or (123 <= ord(s) <= 126): # проверка на спецсимволы
            flag_symbol = True
    
    if flag_ALPHA and flag_alpha and flag_digit and flag_symbol:
        return True
    else:
        return False
      

# strong_password('asdER_12(sad^')
# True
# strong_password('12345678')
# False