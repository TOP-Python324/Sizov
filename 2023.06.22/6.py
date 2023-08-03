from utils import important_message
import data.vars

from pathlib import Path
from sys import path

ROOT_DIR = Path(path[0])
QUESTIONS_PATH = ROOT_DIR / 'data/questions.quiz'

def main() -> None:
    """ управляет работой приложения"""
    
    print(f'{important_message(data.vars.APP_TITLE)}')
    
    data_db = read_questions() 
    print(data_db)
    
def read_questions() -> list:    
    """Читает файл и помещает данные в структуру данных """
    
    data = {}
    # читает файл и парсит данные
    with open(QUESTIONS_PATH, 'r', encoding='utf-8') as filein:
        for line in filein:
            # если не пустая строка
            if len(line) > 1:
                # если первый символ не число то это вопрос
                if line[:1].isalpha():
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
    
main()
    