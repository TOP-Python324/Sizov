from pathlib import Path
from pprint import pprint
from sys import path

# ИСПРАВИТЬ: импорт модулей собственного проекта в общем случае предпочтительнее осуществлять с помощью инструкции import ...
from utils import important_message
import data.vars


# ИСПОЛЬЗОВАТЬ: компактную запись там, где это не вредит читаемости кода
QUESTIONS_PATH = Path(path[0]) / 'data/questions.quiz'

def main() -> None:
    """Управляет работой приложения."""
    print(f'{important_message(data.vars.APP_TITLE)}')
    data_db = read_questions()
    pprint(data_db, sort_dicts=False)


# СДЕЛАТЬ: все вспомогательные функции согласно условию должны быть объявлены в модуле utils
def read_questions() -> list:    
    """Читает файл и помещает данные в структуру данных."""
    data = {}
    # читает файл и парсит данные
    with open(QUESTIONS_PATH, 'r', encoding='utf-8') as filein:
        # ИСПРАВИТЬ: сначала прочитайте текст, затем выйдите из менеджера контекста (что закроет файл), а уже после парсите данные
        for line in filein:
            # если не пустая строка
            if len(line) > 1:
                # если первый символ не число то это вопрос
                if line[:1].isalpha():
                    # ИСПРАВИТЬ: такой срез откусывает последний символ от последней строчки
                    question = line[:-1]
                    data[question] = {}
                # иначе это варианты ответа
                else:
                    # если правильный ответ
                    if line.endswith('+\n'):
                        data[question][line[:-3]] = True
                    else:
                        data[question][line[:-1]] = False
    return data        


# ИСПОЛЬЗОВАТЬ: проверку, что данный модуль является точкой входа, а не импортируемым
if __name__ == '__main__':
    main()


# СДЕЛАТЬ: продолжайте работу
