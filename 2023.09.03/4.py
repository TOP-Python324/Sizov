from pathlib import Path
from sys import path
# ИСПРАВИТЬ: при импорте из стандартной библиотеки и внешних пакетов почти всегда предпочтительнее использовать конструкцию from ... import ...
from csv import reader, writer


class CountableNouns:
    """
    Предоставляет интерфейс для работы с файловой базой существительных.
    """
    # ИСПРАВИТЬ: при передачи в функцию open() относительного пути интерпретатор будет искать файл относительно текущего рабочего каталога (cwd), а не относительно каталога со скриптом (см. тест ниже)
    db_path: Path = Path(r'words.csv')
    script_dir = Path(path[0])
    file_path = script_dir / db_path
    words: dict[str, tuple[str, str]] = {}
    # считывание данных из CSV файла
    with open(file_path, encoding='utf-8') as r_file:
        # УДАЛИТЬ: избыточная переменная file_reader
        for row in reader(r_file, delimiter=','):
            words[row[0]] = (row[1], row[2])

    @classmethod
    def pick(cls, number: int, word: str) -> str:
        """Принимает в качестве аргументов число и существительное для согласования в единственном числе, возвращает согласованное с переданным числом существительное."""
        # ИСПОЛЬЗОВАТЬ:
        try:
            last_digit, two_last_digits = number % 10, number % 100
            if last_digit == 1 and two_last_digits != 11:
                return word
            elif last_digit < 5 and (two_last_digits < 10 or two_last_digits > 19):
                return cls.words[word][0]
            else:
                return cls.words[word][1]
        except KeyError:
            cls.save_words(word)
        
    @classmethod
    def save_words(cls, word1: str = None) -> None:
        """Запрашивает в stdin у пользователя два или три слова согласующихся с числительными, добавляет полученные значения в поле класса words и дописывает их в файл с базой существительных."""
        if word1 is None:
            word1 = input('введите слово, согласующееся с числительным "один": ')
            # ИСПРАВИТЬ: эти действия выполняются одинаково вне зависимости от результата проверки — вынести за пределы условной конструкции
        else:
            print(f'существительное "{word1}" отсутствует в базе')
            
        word2 = input('введите слово, согласующееся с числительным "два": ')
        word5 = input('введите слово, согласующееся с числительным "пять": ')  
        
        cls.words[word1] = (word2, word5)  
        
        # запись данных в CSV файл
        # ИСПРАВИТЬ: в данном случае имеет смысл использовать дозапись в файл, потому что данный метод вызывается только для тех слов, которые отсутствуют в файле
        with open(cls.file_path, 'a', newline='', encoding='utf-8') as csvfile:
            file_writer = writer(csvfile, delimiter=',')
            # КОММЕНТАРИЙ: при дозаписи не придётся итерироваться по всему словарю — при большом количестве элементов это станет весьма затратной процедурой
            file_writer.writerow([word1, word2, word5])
        # УДАЛИТЬ: если нет других вариантов возврата, то в явном возврате None нет необходимости: функция, в которой нет ни одного return, всегда вернёт None  


# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней')}
# >>> CountableNouns.pick(22, 'год')
# 'года'
# >>> CountableNouns.pick(365, 'день')
# 'дней'
# >>> CountableNouns.pick(21, 'попугай')
# 'попугай'
# >>> CountableNouns.pick(22, 'попугай')
# существительное "попугай" отсутствует в базе
# введите слово, согласующееся с числительным "два": попугая
# введите слово, согласующееся с числительным "пять": попугаев
# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней'), 'попугай': ('попугая', 'попугаев')}
# >>>
# >>> CountableNouns.save_words()
# введите слово, согласующееся с числительным "один": капля
# введите слово, согласующееся с числительным "два": капли
# введите слово, согласующееся с числительным "пять": капель
# >>> print(CountableNouns.db_path.read_text(encoding='utf-8'))
# год,года,лет
# месяц,месяца,месяцев
# день,дня,дней
# попугай,попугая,попугаев
# капля,капли,капель

# КОММЕНТАРИЙ: в текущем рабочем каталоге нет файла words.csv
# d:\G-Doc\TOP Academy\Python web\322
#  19:30:14 > dir /b /o:g
# homeworks
# scripts
# projects
# Python322_журнал.xlsx
# logo.png
# HW.txt
#
# d:\G-Doc\TOP Academy\Python web\322
#  19:30:57 > python homeworks\Sizov\2023.08.10\4.py
# Traceback (most recent call last):
#   File "d:\G-Doc\TOP Academy\Python web\322\homeworks\Sizov\2023.08.10\4.py", line 7, in <module>
#     class CountableNouns:
#   File "d:\G-Doc\TOP Academy\Python web\322\homeworks\Sizov\2023.08.10\4.py", line 16, in CountableNouns
#     with open(db_path, encoding='utf-8') as r_file:
#          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: 'words.csv'

# >>> CountableNouns.pick(5, 'слово')
# существительное "слово" отсутствует в базе
# введите слово, согласующееся с числительным "два": слова
# введите слово, согласующееся с числительным "пять": слов
# >>>
# >>> CountableNouns.pick(11, 'слово')
# 'слово'
# >>> CountableNouns.pick(14, 'слово')
# 'слова'


# ИТОГ: нужно лучше, доработать — 4/7

# E:\!Обучение\top\!Python\Sizov>python -i 2023.08.10\4.py
# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней'), 'попугай': ('попугая', 'попугаев'), 'капля': ('капли', 'капель'), 'слово': ('слова', 'слов')}
# >>> CountableNouns.pick(5, 'камень')
# существительное "камень" отсутствует в базе
# введите слово, согласующееся с числительным "два": камня
# введите слово, согласующееся с числительным "пять": камней
# >>>
# >>> CountableNouns.pick(11, 'камень')
# 'камней'
# >>> CountableNouns.pick(112, 'камень')
# 'камней'
# >>> CountableNouns.pick(5119, 'камень')
# 'камней'
# >>>