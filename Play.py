import random

line_abc = ["A", "B", "C"]                                 # Создаем игровое поле при помощи строк и зполняем его
field = [["   "]*3 for i in range(3)]                      # пробелами


def show():
    print("     0     1     2")
    print("  ___________________")

    for i, row in enumerate(field):
        row_str = f"{line_abc[i]} | {' | '.join(row)} |"
        print(row_str)
        print("  |_____|_____|_____|")                     #


def ask():
    while True:                                                             # Функция ввода и анализа введенных данных
        cords = input("Ваш ход:  ").split()
        if len(cords) != 2:
            print("Ошибка ввода: введите два символа")
            continue
        if not(cords[0].isalpha()) or not(cords[1].isdigit()):
            print("Ошибка ввода: введите латинскую букву и цифру")
            continue
        cords[0] = cords[0].upper()                                          # Перевод введенных значений в нужный
        y = int(cords[1])                                                    # формат и последующая обработка

        if cords[0] not in line_abc or 0 > y or y > 2:
            print("Ошибка ввода: введите правильные символы")
            continue
        x = line_abc.index(cords[0])
        if field[x][y] != "   ":
            print("Клетка занята")
            continue

        return x, y


def zero():                                         # генерация для О случайных координат, для ответа на ввод игрока
    while True:
        zero1 = random.randint(0, 2)
        zero2 = random.randint(0, 2)
        if field[zero1][zero2] != "   ":
            continue

        return zero1, zero2


def brains():                                                       # анализ выиграшной комбинации игрока (три Х )
    for i in range(3):
        j = 0

        if field[i][j] == "X  " and field[i][j+1] == "X  " and field[i][j+2] == "X  ":
            print("Вы выиграли")
            return True
    for j in range(3):
        i = 0

        if field[i][j] == "X  " and field[i+1][j] == "X  " and field[i+2][j] == "X  ":
            print("Вы выиграли")
            return True

    if field[0][0] == "X  " and field[1][1] == "X  " and field[2][2] == "X  ":
        print("Вы выиграли")
        return True

    if field[0][2] == "X  " and field[1][1] == "X  " and field[2][0] == "X  ":
        print("Вы выиграли")
        return True


def brains_zero():                                                      # анализ проигранной позиции (три О )
    for i in range(3):
        j = 0

        if field[i][j] == "O  " and field[i][j+1] == "O  " and field[i][j+2] == "O  ":
            print("Вы проиграли")
            return True
    for j in range(3):
        i = 0

        if field[i][j] == "O  " and field[i+1][j] == "O  " and field[i+2][j] == "O  ":
            print("Вы проиграли")
            return True
    if field[0][0] == "O  " and field[1][1] == "O  " and field[2][2] == "O  ":
        print("Вы проиграли")
        return True
    if field[0][2] == "O  " and field[1][1] == "O  " and field[2][0] == "O  ":
        print("Вы проиграли")
        return True


def question():                                                 # функция предлагающая продолжить игру
    end = input("Продолжить?  ")
    if end in "y, Y, н, Н":
        for x in range(3):
            for y in range(3):
                field[x][y] = "   "
        return True


def play():
    print("Добро пожаловать в игру 'Крестики-Нолики'")
    print("Вы играете за 'Крестик'")
    print("Для ввода координат клетки введите  латинскую A, B, или C и цифру через пробел ")
    print("Пример: A 0,   B 2,   C 1")

    count = 0                                                   # count-счетчик ходов
    while True:

        show()                                                  # рисуем поле
        x, y = ask()                                            # спрашиваем координаты

        field[x][y] = "X  "                                      # если все нормально, ставим X

        win = brains()                                           # анализ комбинации Х
        count += 1

        if win:                                                   # если выиграли, то вопрос о продолжении игры
            show()
            if question():
                count = 0                                          # если "да", то обнуление поля, счетчика и выход
                continue                                           # на начало игры
            else:
                break
        if count == 9:                                              # проверка на ничью
            print("Ничья")
            if question():
                count = 0
                continue
            else:
                break

        zero1, zero2 = zero()                                   # Генерация координат О, с дальнейшей проверкой
        field[zero1][zero2] = "O  "                              # на проигрыш игрока
        loss = brains_zero()
        count += 1

        if loss:
            show()
            if question():
                count = 0
                continue
            else:
                break


play()
