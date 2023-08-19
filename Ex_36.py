from sys import exit

# Делаем чек-лист выполненных комнат
check_list = [False, False, False]


def start(back):
    """Функция старт, с которой будет начинаться программа"""

    # Выводим первое приветственное сообщение, при котором пользователь первый раз запускает программу
    if back is not True:
        print('Привет, игрок!\nПеред тобой 3 комнаты, тебе нужно найти выход\nВведи 1, 2 или 3')

    # Выводим сообщение когда завершена комната 1 и 2
    elif back is True and check_list[0] is True and check_list[1] is True:
        print('Отлично, ты закончил 1-ю и 2-ю комнату\nОсталась последняя, выбор очевиден!\nВведи 3')

    # Выводим сообщение когда завершена комната 2
    elif back is True and check_list[1] is True:
        print('Отлично, ты закончил 2-ю комнату\nТеперь выбирай между 1 или 3')

    # Выводим другое сообщение которое будет выводиться при возврате в главную комнату
    elif back is True:
        print('И так, ты решил вернуться\nВсё так же 3 комнаты, выбирай - 1, 2 или 3')

    # Даём пользователю поле, что бы он ввел число
    action = input('> ')

    # Делаем проверку точно ли пользователь ввёл число, а так же делаем ветки для выбора комнаты
    if not action.isdigit():
        print('Нужно ввести цифру, не более')
    elif action == '1':
        first_room()

    # Делаем проверку, что бы пользователь не зашел в комнату повторно
    elif action == '1' and check_list[0] is True:
        print('Ты эту комнату уже завершил, больше туда зайти нельзя')
    elif action == '2':
        second_room()

    # Делаем проверку, что бы пользователь не зашел в комнату повторно
    elif action == '2' and check_list[1] is True:
        print('Ты эту комнату уже завершил, больше туда зайти нельзя')
    elif action == '3':
        third_room()


def death(sentence):
    """Функция смерти. Будет выводить сообщение и выходить с программы"""
    print(sentence, '\nНу если вкратце, то ты умер')
    exit(0)


def second_room():
    """Функция второй комнаты, тут будет бурый медведь"""

    # Выводим приветственное сообщение второй комнаты
    print(
        'Ты сейчас находишься в комнате с бурым медведем\nК твоему счастью, он спит. Но в руках он держит какую-то глиняную вазу')

    # Даём пользователю выбор между действиями
    print('Ты можешь попытаться тихо посмотреть что в вазе или быстро выхватить вазу и убежать\nВыбирай - 1 или 2')

    # Делаем булевую переменную, что бы не делать много веток if else
    action_next = False

    # Так же делаем бесконечный цикл для тех же моментов
    while True:

        # Даём поле, что бы он ввёл число
        action = input('> ')

        # Делаем проверку точно ли пользователь ввёл число, а так же делаем ветки для выбора
        if not action.isdigit():
            print('Нужно ввести цифру, не более')
        elif action == '1' and action_next is False:
            action_next = True
            print('Ты подходишь к медведю, смотришь в вазу, там мед\nНо на дне ты видишь ключ БИНГО')
            print('Ты можешь аккуратно достать ключ или же вытащить вазу у медведя\nВыбирай - 1 или 2')
        elif action == '1' and action_next is True:
            print(
                'Ты суёшь руку в мед, и достаешь ключ, отлично!\nС этой комнатой ты разобрался!\nДверь открылась и ты выходишь')
            check_list[1] = True
            start(True)
        elif action == '2' and action_next is False:
            death(
                'Ты стремительно идешь к медведю, уверенно вырываешь банку, идешь к выходу, а дверь закрыта, и как раз медведь проснулся')
        elif action == '2' and action_next is True:
            death('Ты пытаешься вытащить вазу с рук медведя, но ты это делал не аккуратно и он проснулся')


def first_room():
    """Функция первой комнаты, тут будет сундук"""

    if check_list[1] is False:

        # Выводим приветственное сообщение первой комнаты
        print(
            'В комнате голые стены без окон, по средине стоит сундук, для него нужен ключ\nЕсть вариант поискать в комнате, или вернуться потом и поискать в других комнатах\nВыбирай - 1 или 2')
    else:

        # Если игрок нашел ключ, мы ему дадим выбор открыть сундук
        print(
            'В комнате голые стены без окон, по средине стоит сундук, для него нужен ключ\nУ тебя как раз есть один, стоит проверить\nВведи 1 что бы открыть сундук')

    # Делаем бесконечный цикл что бы зациклить выбор (делается для <elif choice == '1':>)
    while True:

        # Даём пользователю поле, что бы он ввел число
        action = input('> ')

        # Делаем проверку точно ли пользователь ввёл число, а так же делаем ветки для выбора
        if not action.isdigit():
            print('Нужно ввести цифру, не более')
        elif action == '1' and check_list[1] is True:
            print(
                'УРАААА, у тебя получилось открыть сундук, в нем еще один ключ\nКЛАССС\nЯ думаю ты найдешь ему применение, а так же я тебя поздравляю, ты закончил и эту комнату')
            check_list[0] = True
            start(True)
        elif action == '1':
            print('Ты ничего не нашел, в комнате пусто\nТы только зря потратил время')
        elif action == '2':
            start(True)


def third_room():
    """Функция третьей комнаты, тут же и будет выход и победа"""

    # Если ты не выполнил 2 предыдущие комнаты, то ты не сможешь открыть дверь
    if check_list[0] is False and check_list[1] is False:
        print(
            'Ты подходишь к двери, но она не открывается\nТы дёргаешь за ручку, но она не поддаётся\nТы видишь замочную скважину внизу ручки, нужен ключ')
        start(True)

    # Концовка игры
    elif check_list[0] is True and check_list[1] is True:
        print(
            'Ты подходишь к двери, но она не открывается\nТы дёргаешь за ручку, но она не поддаётся\nТы видишь замочную скважину внизу ручки, нужен ключ\nТы как раз с собой имеешь один\nИ, О ЧУДО, ты открыл дверь, и он ведет к выходу, УРАААААА\n\nНапиши разработчику в телеграмме, под ником @IONEKIS, слово собака, и он тебе даст кое-что приятное')
        exit(0)

    # Если ты выполнил комнату 2, то ты не сможешь открыть дверь, потому что ключ не подходит
    elif check_list[1] is True:
        print(
            'Ты подходишь к двери, но она не открывается\nТы дёргаешь за ручку, но она не поддаётся\nТы видишь замочную скважину внизу ручки, нужен ключ\nТы как раз с собой имеешь один\nНо он намного больше чем скважина, он попросту не пролезет, нужен другой ключ')
        start(True)


# Запускаем программу
start(False)