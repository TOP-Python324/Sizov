from utils import important_message

def main() -> None:
    message = input('введите сообщение: ')
    print(f'\n{important_message(message)}\n')
    return None