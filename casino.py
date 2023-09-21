# Файл запуска игры
from decouple import config # для считывания значения по ключу из файла: settings.ini
from casino_logics import play_game # для считывания логики игры

# print(config('MY_MONEY'))

if __name__ == '__main__':
    initial_money = int(config('MY_MONEY'))
    current_money = play_game(initial_money)
    print(f'Result: You have: {current_money} soms')
