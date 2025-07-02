EN = 'abcdefghijklmnopqrstuvwxyz'
RU = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

alphabet = ''
string = ''
mode = 0
rot = 0

def init():
    global mode 
    global alphabet
    global string
    global rot 

    print('1 - Кодирование\n2 - Декодирование')
    if int(input()) == 1:
        mode = 1
    else:
        mode = -1

    print('Введите строку:')
    string = input()

    print('Язык алфавита:\n1 - Английский\n2 - Русский')
    if int(input()) == 1:
        alphabet = EN
    else:   
        alphabet = RU

    print('Сдвиг:')
    rot = int(input())

def code():
    result = ''
    for letter in string:
        if letter.islower():
            result += alphabet[(rot * mode + alphabet.find(letter)) % len(alphabet)]
        elif letter.isupper():
            result += alphabet[(rot * mode + alphabet.find(letter.swapcase())) % len(alphabet)].swapcase()
        else:
            result += letter
    return result

init()
print(code())