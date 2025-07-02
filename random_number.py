from random import randint

LEFT_VALUE = 1
RIGHT_VALUE = 100

goal_number = randint(LEFT_VALUE, RIGHT_VALUE)

print('Добро пожаловать в числовую угадайку')

def is_valid(value: str):
    if value.isdigit():
        return LEFT_VALUE <= int(value) <= RIGHT_VALUE
    else:
        return False

def check_number(number):
    if number == goal_number:
        print('Вы угадали, поздравляем!')
    elif number > goal_number:
        print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print('Ваше число меньше загаданного, попробуйте еще разок')

while True:
    string = input(f'Введите целое число от {LEFT_VALUE} до {RIGHT_VALUE} (включительно) : ')
    if is_valid(string):
        enter_number = int(string)
        check_number(enter_number)

    else:
        print('Неверный формат данных')


    


