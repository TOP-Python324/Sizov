from pathlib import Path
from sys import path
# ИСПРАВИТЬ: при импорте из стандартной библиотеки и внешних пакетов почти всегда предпочтительнее использовать конструкцию from ... import ...
import csv


class CountableNouns:
    """
    Предоставляет интерфейс для работы с файловой базой существительных.
    """
    # ИСПРАВИТЬ: при передачи в функцию open() относительного пути интерпретатор будет искать файл относительно текущего рабочего каталога (cwd), а не относительно каталога со скриптом (см. тест ниже)
    db_path: Path = Path(r'words.csv')
    words: dict[str, tuple[str, str]] = {}
    # считывание данных из CSV файла
    with open(db_path, encoding='utf-8') as r_file:
        # УДАЛИТЬ: избыточная переменная file_reader
        file_reader = csv.reader(r_file, delimiter=',')
        for row in file_reader:
            words[row[0]] = (row[1], row[2])

    @classmethod
    def pick(cls, number: int, word: str) -> str:
        """Принимает в качестве аргументов число и существительное для согласования в единственном числе, возвращает согласованное с переданным числом существительное."""
        # ИСПРАВИТЬ: смотреть одну последнюю цифру недостаточно, потому что есть числа исключения из правил согласования: 11, 12, 13, 14 и прочие, заканчивающиеся на эти цифры (см. тест ниже)
        number = number if number < 10 else number % 10
        # ИСПРАВИТЬ: в данном случае имеет смысл использовать перехват исключения KeyError
        if number == 1:
            return word
        else: 
            if word in cls.words:
                if number < 5:
                    return cls.words[word][0]
                else:
                    return cls.words[word][1]    
            else:
                cls.save_words(word)
        
    @classmethod
    def save_words(cls, word1: str = None) -> None:
        """Запрашивает в stdin у пользователя два или три слова согласующихся с числительными, добавляет полученные значения в поле класса words и дописывает их в файл с базой существительных"""
        if word1 is None:
            word1 = input('введите слово, согласующееся с числительным "один": ')
            # ИСПРАВИТЬ: эти действия выполняются одинаково вне зависимости от результата проверки — вынести за пределы условной конструкции
            word2 = input('введите слово, согласующееся с числительным "два": ')
            word5 = input('введите слово, согласующееся с числительным "пять": ')
        else:
            print(f'существительное "{word1}" отсутствует в базе')
            word2 = input('введите слово, согласующееся с числительным "два": ')
            word5 = input('введите слово, согласующееся с числительным "пять": ')
            
        cls.words[word1] = (word2, word5)  
        
        # запись данных в CSV файл
        # ИСПРАВИТЬ: в данном случае имеет смысл использовать дозапись в файл, потому что данный метод вызывается только для тех слов, которые отсутствуют в файле
        with open(cls.db_path, 'w', newline='', encoding='utf-8') as csvfile:
            file_writer = csv.writer(csvfile, delimiter=',')
            # КОММЕНТАРИЙ: при дозаписи не придётся итерироваться по всему словарю — при большом количестве элементов это станет весьма затратной процедурой
            for word in cls.words:
                file_writer.writerow([word, cls.words[word][0], cls.words[word][1]])
        # УДАЛИТЬ: если нет других вариантов возврата, то в явном возврате None нет необходимости: функция, в которой нет ни одного return, всегда вернёт None
        return None    


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
