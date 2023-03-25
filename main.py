from random import randint


def attack(char_name, char_class):
    if char_class == 'warrior':
        damage = 5 + randint(3, 5)
    elif char_class == 'mage':
        damage = 5 + randint(5, 10)
    elif char_class == 'healer':
        damage = 5 + randint(-3, -1)
    else:
        damage = 0
    if damage:
        return f'{char_name} нанёс урон противнику равный {damage}'
    return f'{char_name} не нанёс урон противнику'


def defence(char_name, char_class):
    if char_class == 'warrior':
        damage = 10 + randint(5, 10)
    elif char_class == 'mage':
        damage = 10 + randint(-2, 2)
    elif char_class == 'healer':
        damage = 10 + randint(2, 5)
    else:
        damage = 0
    if damage:
        return f'{char_name} блокировал {damage} урона'
    return f'{char_name} не смог блокировать урон'


def special(char_name, char_class):
    if char_class == 'warrior':
        value = 80 + 25
    elif char_class == 'mage':
        value = 5 + 40
    elif char_class == 'healer':
        value = 10 + 30
    else:
        value = 0
    if value:
        return f'{char_name} применил специальное умение «Защита {value}»'
    return f'{char_name} не применил специальное умение'


def start_training(char_name, char_class):
    if char_class == 'warrior':
        class_description = 'Воитель — отличный боец ближнего боя.'
    elif char_class == 'mage':
        class_description = 'Маг — превосходный укротитель стихий.'
    elif char_class == 'healer':
        class_description = 'Лекарь — чародей, способный исцелять раны.'
    else:
        class_description = ''

    if class_description:
        print(f'{char_name}, ты {class_description}')
    else:
        print('Такой персонажа пока не доступен, но мы учтём твои пожелания.')
        char_class = choice_class()
        print(start_training(char_name, char_class))

    print('Потренируйся управлять своими навыками.')
    show_training_rules()
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        elif cmd == 'defence':
            print(defence(char_name, char_class))
        elif cmd == 'special':
            print(special(char_name, char_class))
        else:
            show_training_rules()
    return 'Тренировка окончена.'


def choice_class():
    request_message = 'Введи название персонажа, за которого хочешь играть'
    available_classes = 'Воитель — warrior, Маг — mage, Лекарь — healer'
    return input(f'{request_message}: {available_classes}: ')


def show_training_rules():
    commands = (
        'attack — чтобы атаковать противника, '
        'defence — чтобы блокировать атаку противника '
        'или special — чтобы использовать свою суперсилу'
    )
    print(f'Введи одну из команд: {commands}.')
    print('Если не хочешь тренироваться, введи команду skip.')


def choice_char_class():
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = choice_class()
        if char_class == 'warrior':
            print(
                'Воитель — дерзкий воин ближнего боя. '
                'Сильный, выносливый и отважный.'
            )
        elif char_class == 'mage':
            print(
                'Маг — находчивый воин дальнего боя. '
                'Обладает высоким интеллектом.'
            )
        elif char_class == 'healer':
            print(
                'Лекарь — могущественный заклинатель. '
                'Черпает силы из природы, веры и духов.'
            )
        else:
            choice_char_class()
        approve_choice = input(
            'Нажми (Y), чтобы подтвердить выбор, '
            'или любую другую кнопку, '
            'чтобы выбрать другого персонажа '
        ).lower()
    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')

    char_name = input('...назови себя: ')
    status = 'Сейчас твоя выносливость — 80, атака — 5 и защита — 10'

    print(f'Здравствуй, {char_name}! {status}.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')

    char_class = choice_char_class()

    print(start_training(char_name, char_class))


main()
