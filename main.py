import random


def main():
    print('Добро пожаловать в числовую угадайку')
    print()
    border = int(input('В каком диапазоне будем угадывать? от 1 до '))
    num = random.randint(1, border + 1)
    print()
    print(num)
    print()
    enter(input(f'введите число от 1 до {border}'), num, border)


def enter(n, num, border):
    is_valid(n, num, border)


def is_valid(n, num, border):
    try:
        if int(n) in range(1, border + 1):
            return comparing_numbers(int(n), num, border)
        else:
            return enter(input(f'А может быть все-таки введем целое число от 1 до {border}?'), num, border)
    except:
        return enter(input(f'А может быть все-таки введем целое число от 1 до {border}?'), num, border)


def comparing_numbers(n, num, border):
    count = 1
    if n == num:
        print(f'Вы угадали. поздравляем!', '', f'Попыток использованно - {count}.')
        answer = (input('Сыграем еще разок? (д/н)'))
        if answer in ['y', 'l', 'н', 'д']:
            return main()
        else:
            print('', 'Спасибо, что играли в числовую угадайку. Еще увидимся...', sep='\n')
    elif n > num:
        count += 1
        return enter(input('Ваше число больше загаданного, попробуйте еще разок'), num, border)
    else:
        count += 1
        return enter(input('Ваше число меньше загаданного, попробуйте еще разок'), num, border)


main()
