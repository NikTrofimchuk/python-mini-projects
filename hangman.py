import random

word_list = ['чел', 'авто', 'мужик', 'кириллица', 'телка', 'восемь', 'потеря', 'пассат', 'автозвук', 'суицид']

option = 1

def get_word():
    return word_list[random.randint(0, len(word_list) - 1)].upper()

def display_hangman(tries):
    stages = [
        # финальное состояние: голова, торс, обе руки, обе ноги
        '''
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
            -
        ''',
        # голова, торс, обе руки, одна нога
        '''
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / 
            -
        ''',
        # голова, торс, обе руки
        '''
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |      
            -
        ''',
        # голова, торс и одна рука
        '''
            --------
            |      |
            |      O
            |     \\|
            |      |
            |     
            -
        ''',
        # голова и торс
        '''
            --------
            |      |
            |      O
            |      |
            |      |
            |     
            -
        ''',
        # голова
        '''
            --------
            |      |
            |      O
            |    
            |      
            |     
            -
        ''',
        # начальное состояние
        '''
            --------
            |      |
            |      
            |    
            |      
            |     
            -
        '''
    ]
    return stages[tries]

def validation(enter):
    if enter.isalpha():
        return enter.upper()
    while not enter.isalpha():
        print('Введите строку содержащую только буквы')
        enter = input()
    return enter.upper()
    
def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток

    if tries == 6:
        print('Давай играть!')

    while True:
        print(display_hangman(tries))
        if tries == 0:
            break
        print(word_completion)
        print('Введите слово или букву')
        entering_data = validation(input())

        if entering_data in guessed_letters or entering_data in guessed_words:
            print('Вы уже загадывали данное слово либо букву')
            continue

        if len(entering_data) == 1:
            for i in range(len(word)):
                if entering_data == word[i]:
                    word_completion = word_completion[:i] + entering_data + word_completion[i + 1:]
            if word_completion == word:
                guessed = True
                break  
            guessed_letters.append(entering_data)

        else:
            if word == entering_data:
                guessed = True
                break
            else:
                guessed_words.append(entering_data)
        
        tries -= 1
    if guessed:
        print('Поздравляем вы угадали все слово!')
    else:
        print('Сожалеем но вы проиграли(')
        print('Загаданное слово: ', word)

while option == 1:
    word = get_word()
    play(word)
    print('Начать заново?\n1 - Еще попытка\n2 - Выход из программы')
    option = int(input())