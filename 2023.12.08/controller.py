"""
Controller (MVC): управляющий модуль.
"""

import model
import view


class Application():
    """
    Осуществляет взаимодействие между моделью и представлением.
    """

    @staticmethod
    def save_email(email: str) -> None:
        """Сохраняет email адрес в файл."""
        model.FileIO.add_email(email)
        view.CLI.email_save(email)


    @staticmethod
    def get_email() -> None:
        "Запрашивает email у пользователя"
        while True:
            email: str = view.CLI.email_input()    
            if email == '':
                break
            else:
                try: 
                    instance = model.Email(email)
                    Application.save_email(email)
                except ValueError:
                    view.CLI.email_error()
                    print('Повторите ввод')