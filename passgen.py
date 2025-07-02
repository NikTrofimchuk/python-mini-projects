import random

DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SYMBOLS = 'il1Lo0O'
result_str = ''

def generate_password(pass_len, result):
    password = ''
    i = 0
    for i in range(pass_len):
        rand_pos = random.randint(0, len(result) - 1)
        password += result[rand_pos]
    print(password)

print('Количество паролей:')
pass_count = int(input())

print('Длина одного пароля')
pass_len = int(input())

print('Включать ли цифры?\n1 - Да, 2 - Нет')
if int(input()) == 1:
    result_str += DIGITS

print('Включать ли прописные буквы?\n1 - Да, 2 - Нет')
if int(input()) == 1:
    result_str += UPPERCASE_LETTERS

print('Включать ли строчные буквы?\n1 - Да, 2 - Нет')
if int(input()) == 1:
    result_str += LOWERCASE_LETTERS
print('Включать ли символы?\n1 - Да, 2 - Нет')
if int(input()) == 1:
    result_str += SYMBOLS

i = 0
for i in range(pass_count):
    generate_password(pass_len, result_str)