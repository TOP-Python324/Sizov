"""
View (MVC): представление с интерфейсом командной строки.
"""

class CLI():
    """
    Ввод/вывод данных через командную строку.
    """

    @staticmethod
    def email_input() -> str:
        """Запрашивает у пользователя email адрес."""
        return input("\n Введите email > ")


    @staticmethod
    def email_error() -> None:
        """Выводит сообщение о некорректном адресе."""
        print('email введен не корректно!')


    @staticmethod
    def email_save(email: str) -> None:
        """Выводит сообщение об успешном сохранении адреса."""
        print(f'Email {email} сохранен!')