from random import randint

from graphic_arts.start_game_banner import run_screensaver

DEFAULT_ATTACK: int = 5
DEFAULT_DEFENCE: int = 10
DEFAULT_STAMINA: int = 80


class Character:
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'
    RANGE_VALUE_ATTACK: tuple = (1, 3)
    RANGE_VALUE_DEFENCE: tuple = (1, 5)
    SPECIAL_BUFF: int = 15
    SPECIAL_SKILL: str = 'Удача'

    def __init__(self, name: str):
        self.name: str = name

    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'

    def attack(self) -> str:
        """Return a message about the damage caused by the character."""
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return f'{self.name} нанёс противнику урон, равный {value_attack}'

    def defence(self) -> str:
        """
        Return a message about the damage blocked by the character.
        """
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return f'{self.name} блокировал {value_defence} ед. урона.'

    def special(self) -> str:
        """Return a message about a special skill applied by the character."""
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS: str = (' дерзкий воин ближнего боя. '
                                  'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK: tuple = (3, 5)
    RANGE_VALUE_DEFENCE: tuple = (5, 10)
    SPECIAL_BUFF: int = DEFAULT_STAMINA + 25
    SPECIAL_SKILL: str = 'Выносливость'

    def __init__(self, name):
        super().__init__(name)


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS: str = (' находчивый воин дальнего боя. '
                                  'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK: tuple = (5, 10)
    RANGE_VALUE_DEFENCE: tuple = (-2, 2)
    SPECIAL_BUFF: int = DEFAULT_ATTACK + 40
    SPECIAL_SKILL: str = 'Атака'

    def __init__(self, name):
        super().__init__(name)


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS: str = (' могущественный заклинатель. '
                                  'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK: tuple = (-3, -1)
    RANGE_VALUE_DEFENCE: tuple = (2, 5)
    SPECIAL_BUFF: int = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL: str = 'Защита'

    def __init__(self, name):
        super().__init__(name)


def choice_char_class(char_name: str) -> Character:
    """
    Return the selected class the player will play as.
    Checks if the class is available for selection, asks for confirmation.
    """
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}

    approve_choice: str = ''

    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                               'за которого хочешь играть: Воитель — warrior, '
                               'Маг — mage, Лекарь — healer: ')
        if selected_class in game_classes:
            char_class: Character = game_classes[selected_class](char_name)
            print(char_class)
            approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                                   'или любую другую кнопку, '
                                   'чтобы выбрать другого персонажа ').lower()
    return char_class


def start_training(character: Character) -> str:
    """Start training"""
    training_commands = {
        'attack': character.attack,
        'defence': character.defence,
        'special': character.special,
    }
    show_training_rules()
    selected_command: str = ''
    while selected_command != 'skip':
        selected_command = input('Введите команду: ').lower()
        if selected_command in training_commands:
            print(training_commands[selected_command]())
        else:
            show_training_rules()
    return 'Тренировка окончена.'


def show_training_rules() -> None:
    """Display commands available for training."""
    print('Потренируйся управлять своими навыками.')
    commands: str = (
        'attack — чтобы атаковать противника, '
        'defence — чтобы блокировать атаку противника '
        'или special — чтобы использовать свою суперсилу'
    )
    print(f'Введи одну из команд: {commands}.')
    print('Если не хочешь тренироваться, введи команду "skip".')


if __name__ == '__main__':
    """Start the game."""
    run_screensaver()

    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    character_name: str = input('...назови себя: ')

    print(f'Здравствуй, {character_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    character_class: Character = choice_char_class(character_name)

    print(start_training(character_class))
