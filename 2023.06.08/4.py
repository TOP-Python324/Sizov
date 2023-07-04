def countable_nouns(number: int, tuples: tuple[str, str, str]) -> str:
    """Возвращает существительное русского языка, согласованное с числом"""
    
    if int(repr(number)[-1]) == 1 and number != 11:
        return tuples[0]    
    elif int(repr(number)[-1]) <= 4 and (number <= 4 or number > 14):
        return tuples[1]
    else:
        return tuples[2]


# >>> countable_nouns(1, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(2, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(10, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(12, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(22, ("год", "года", "лет"))
# 'года'

