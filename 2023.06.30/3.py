from datetime import date
from random import choice, sample, randrange as rr
from pathlib import Path
from re import compile
from sys import path

SCRIPT_DIR = Path(path[0])

pattern1 = compile(r'\W+')

names = {
    'имена': {'мужской': [], 'женский': []},
    'отчества': {'мужской': [], 'женский': []},
    'фамилии': {'мужской': [], 'женский': []},
}

days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def load_data() -> None:
    """Читает из файлов данные и упорядочивает их."""
    m_names_path = SCRIPT_DIR / 'мужские_имена_отчества.txt'
    f_names_path = SCRIPT_DIR / 'женские_имена.txt'
    lastnames_path = SCRIPT_DIR / 'фамилии.txt'
    
    names['имена']['женский'] = f_names_path.read_text(encoding='utf-8').split('\n')
    
    raw_m_names = m_names_path.read_text(encoding='utf-8').split('\n')
    
    for line in raw_m_names:
        name, pat_m, pat_f, *_ = pattern1.split(line)
        names['имена']['мужской'] += [name]
        names['отчества']['мужской'] += [pat_m]
        names['отчества']['женский'] += [pat_f]
        
    raw_lastnames = lastnames_path.read_text(encoding='utf-8').split('\n')
    for line in raw_lastnames:
        try:
            lastn_m, lastn_f = line.split(', ') 
            names['фамилии']['мужской'] += [lastn_m]
            names['фамилии']['женский'] += [lastn_f]
        except ValueError:
            names['фамилии']['мужской'] += [line]
            names['фамилии']['женский'] += [line]
         
def generate_person() -> dict[str]:
    """Генерирует анкету человека со случайными данными."""  
    
    person = {}
#        'имя': str = ''
#        'отчество': str = ''
#        'фамилия': str = ''
#        'пол': types.Literal['мужской', 'женский']
#        'дата рождения': datetime.date
#        'мобильный': str = ''
#    }  
    gender = choice(['мужской', 'женский'])
    
    person['имя'] = choice(names['имена'][gender])
    person['отчество'] = choice(names['отчества'][gender])
    person['фамилия'] = choice(names['фамилии'][gender])
    person['пол']  = gender
    
    year = rr(1923, 2023)
    month = rr(1, 13)
    # проверка на високосный год
    if month == 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        day = rr(1, 30)
    else:    
        day = rr(1, days[month]+1)
    person['дата рождения']  =  date(year, month, day)
    
    tel_number = sample(['1','2','3','4','5','6','7','8','9','0'],9)

    person['мобильный']  = '+79'
    for i in tel_number:
        person['мобильный']  += i
    
    return person
    
# >>> load_data()
# >>> generate_person()
# {'имя': 'Полетта', 'отчество': 'Пантелеевна', 'фамилия': 'Федотова', 'пол': 'женский', 'дата рождения': datetime.date(1928, 4, 11), 'мобильный': '+79237861509'}
# >>> from pprint import pprint
# >>> pprint(generate_person(), sort_dicts=False)
# {'имя': 'Севастьяна',
#  'отчество': 'Захаровна',
#  'фамилия': 'Муромцева',
#  'пол': 'женский',
#  'дата рождения': datetime.date(2010, 11, 17),
#  'мобильный': '+79639475128'}
# >>> pprint(generate_person(), sort_dicts=False)
# {'имя': 'Наркис',
#  'отчество': 'Авдиевич',
#  'фамилия': 'Державин',
#  'пол': 'мужской',
#  'дата рождения': datetime.date(1985, 10, 24),
#  'мобильный': '+79852179034'}
# >>>

    