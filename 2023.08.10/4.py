from pathlib import Path
from sys import path
import csv


class CountableNouns:
    """
    Предоставляет интерфейс для работы с файловой базой существительных.
    """
    db_path: Path = Path(r'words.csv')
    words: dict[str, tuple[str, str]] = {}
    
    # считывание данных из CSV файла
    with open(db_path, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=',')
        for row in file_reader:
            words[row[0]] = (row[1], row[2])

    @classmethod
    def pick(cls, number: int, word: str) -> str:
        """Принимает в качестве аргументов число и существительное для согласования в единственном числе, возвращает согласованное с переданным числом существительное."""
        number = number if number < 10 else number % 10
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
            word2 = input('введите слово, согласующееся с числительным "два": ')
            word5 = input('введите слово, согласующееся с числительным "пять": ')
        else:
            print(f'существительное "{word1}" отсутствует в базе')
            word2 = input('введите слово, согласующееся с числительным "два": ')
            word5 = input('введите слово, согласующееся с числительным "пять": ')
            
        cls.words[word1] = (word2, word5)  
        
        # запись данных в CSV файл
        with open(cls.db_path, 'w', newline='', encoding='utf-8') as csvfile:
            file_writer = csv.writer(csvfile, delimiter=',')
            for word in cls.words:
                file_writer.writerow([word, cls.words[word][0], cls.words[word][1]])
            
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

