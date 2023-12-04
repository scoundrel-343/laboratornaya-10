import random
import logging

logging.basicConfig(filename='Ugadaika.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# Функция для ввода
def user_interaction():
    while True:
        try:
            N = int(input("Введите максимальное число для загадывания: "))
            k = int(input("Введите количество попыток: "))
            if N < 1 or k < 1:
                print("Некорректный ввод. Пожалуйста, введите положительные числа, которые больше 0.")
                logging.error(f"! Ошибка! Некорректный ввод: {N}, {k}")
            else:
                return N, k
        except ValueError:
            print("! Ошибка ! Пожалуйста, введите натуральные числа.")
            logging.error(f"! Ошибка! Некорректный ввод: {N}, {k}")

# Функция для запуска игры
def play_guessing_game(N, k):
    secret_number = random.randint(1, N)
    logging.info(f'Компьютер загадал число от 1 до {N} ({secret_number}). Количество попыток: {k}')

    print(f"Компьютер загадал число от 1 до {N}. Количество попыток: {k}.")

    for attempt in range(1, k + 1):
        guess = int(input(f"Попытка {attempt}. Угадайте число: "))
        logging.info(f'Попытка {attempt}: {guess}')

        if guess < secret_number:
            print("Загаданное число больше!")
            logging.info("Загаданное число больше!")
        elif guess > secret_number:
            print("Загаданное число меньше!")
            logging.info("Загаданное число меньше!")
        else:
            print("Вы угадали!")
            logging.info('Игра завершена: победа')
            return

    print(f"Попытки закончились. Загаданное число было: {secret_number}")
    logging.info('Игра завершена: проигрыш')

if __name__ == "__main__":
    N, k = user_interaction()
    play_guessing_game(N, k)
