# объявление функции
def is_pangram(text):
    sum = 0
    text = text.lower()
    for i in range(len(text)):
        letter = text[i]
        if letter not in text[:i] and letter != ' ':
            sum += 1
    print(sum)
    return sum == 26

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))