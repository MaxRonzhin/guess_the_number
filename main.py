import random

NUM = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')
# print()
# print(NUM)
print()


def enter(n):
    is_valid(n)


def is_valid(n):
    try:
        if int(n) in range(1, 101):
            return comparing_numbers(int(n))
        else:
            return enter(input('А может быть все-таки введем целое число от 1 до 100?'))
    except:
        return enter(input('А может быть все-таки введем целое число от 1 до 100?'))


def comparing_numbers(n):
    if n == NUM:
        print('Вы угадали, поздравляем!', '', 'Спасибо, что играли в числовую угадайку. Еще увидимся...', sep='\n')
    elif n > NUM:
        return enter(input('Ваше число больше загаданного, попробуйте еще разок'))
    else:
        return enter(input('Ваше число меньше загаданного, попробуйте еще разок'))


enter(input('введите число от 1 до 100'))
