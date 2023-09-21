# Логика выигрыша или проигрыша
import random
from decouple import config # для считывания значения по ключу из файла: settings.ini

def play_game(current_money):
    while current_money > 0:
        # Показываем текущий баланс и просим ввести сумму ставки
        bet = int(input(f'Your current amount of money: {current_money} som, Make your bet: '))
        # Вводим условие если ставка превышает текущий баланс
        if bet > current_money:
            print('Insufficient amount of money for the bet')
            # Вводим условие чтобы не было ошибки и игра продолжалась
            continue

        # Просим выбрать номер слота
        make_slot_choice = int(input('Choose slot number from 1 to 30: '))
        # Вводим рандомный выбор выигрышного номера через randint(указываем диапазон)
        winning_slot = random.randint(1,30)

        # Вводим условия выигрыша и проигрыша
        if make_slot_choice == winning_slot:
            current_money += bet * 36
            print(f'Congratulation! You won {bet * 36} soms')
        else:
            current_money -= bet

        # После каждой ставки вам задается вопрос хотите ли вы сыграть еще
        play_again = input("Do you want to play again? (Yes/No): ").capitalize()
        # Вводим условие в случае отказа продолжать игру
        if play_again != "Yes":
            break

    # Вводим опцию повторной игры
    return current_money
