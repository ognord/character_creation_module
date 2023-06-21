from random import randint


def attack(char_name, char_class):
    attack_dict = {
        'warrior': (3, 5),
        'mage': (5, 10),
        'healer': (-3, -1),
    }
    if char_class in attack_dict:
        min_val, max_val = attack_dict[char_class]
    else:
        raise ValueError(f'Character class {char_class} not recognized')
    return (f'{char_name} нанёс урон противнику равный '
            f'{5 + randint(min_val, max_val)}')


def defence(char_name, char_class):
    defence_dict = {
        'warrior': (5, 10),
        'mage': (-2, 2),
        'healer': (2, 5),
    }
    if char_class in defence_dict:
        min_val, max_val = defence_dict[char_class]
    else:
        raise ValueError(f'Character class {char_class} not recognized')
    return (f'{char_name} блокировал '
            f'{10 + randint(5, 10)} урона')


def special(char_name, char_class):
    special_dict = {
        'warrior': ('Выносливость', 105),
        'mage': ('Атака', 45),
        'healer': ('Защита', 40),
    }

    if char_class in special_dict:
        skill, value = special_dict[char_class]
    else:
        raise ValueError(f'Character class {char_class} not recognized')
    return (f'{char_name} применил специальное умение '
            f'«{skill} {value}»')


def start_training(char_name, char_class):
    start_dict = {
        'warrior': 'ты Воитель — отличный боец ближнего боя.',
        'mage': 'ты Маг — превосходный укротитель стихий.',
        'healer': 'ты Лекарь — чародей, способный исцелять раны.'

    }
    if char_class in start_dict:
        print(f'{char_name}, {start_dict[char_class]}')
    else:
        raise ValueError(f'Character class {char_class} not recognized')

    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или special — '
          'чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input(
            'Введи название персонажа, за которого хочешь играть: '
            'Воитель — warrior, Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print(
                'Лекарь — могущественный заклинатель. '
                'Черпает силы из природы, веры и духов.')
        approve_choice = input(
            'Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку, '
            'чтобы выбрать другого персонажа ').lower()
    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))


main()

