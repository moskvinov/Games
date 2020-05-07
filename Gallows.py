import random

# Тут храним отрисовку человечка
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']

# Читаем из файлика слова и заталкиваем их в список
words = []
with open('Word_for_Gallows.txt', 'r') as f:
    words = f.read().splitlines()


def getRandomWord(wordList):
    # Эта функция возвращает случайную строку из переданного списка.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


# Функция отрисовки. Сюда передаются списки некорректных букв, корректных букв и само слово, которое надо отгадать
def displayBoard(missedLetters, correctLetters, secretWord):
    # В зависимости от длины списка, в котором есть неправильные буквы (т.е.) кол-во неправильных попыток, будет рисоваться
    # соответственная часть человечка из списка Hangman_pics
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    # Выводим буквы, которые уже вводили и они были некорректны
    print('Ошибочные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    # len(secretWord) - считаем количество букв в загаданном слове и столько '_' пишем в переменную blanks
    blanks = '_' * len(secretWord)

    # заменяет пропуски отгаданными буквами
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:
                                                  ]
    # Показывает секретное слово с пробелами между буквами
    for letter in blanks:
        print(letter, end=' ')
    print()


def getGuess(letters_list):
    # Возвращает букву, введенную игроком. Эта функция проверяет, что игрок ввел только одну букву и ничего больше.
    while True:
        print('Введите букву.')
        letter = input()
        letter = letter.lower()  # переводим все буквы, которые ввел пользователь в нижний регистр
        if len(letter) != 1:
            print('Пожалуйста, введите одну букву.')
        elif letter in letters_list:
            print('Вы уже называли эту букву. Назовите другую.')
        elif letter not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите БУКВУ.')
        else:
            return letter


def playAgain():
    # Эта функция возвращает значение True, если игрок хочет сыграть заново; в противном случае возвращает False.
    print('Хотите сыграть еще? (да или нет)')
    return input().lower().startswith('д')


# ======================================================================================================================
# тело программы
print('В И С Е Л И Ц А')

# Выбираем уровень сложности. В зависимости от выбранного уровня удаляются "лишние" отрисовки из виселицы.
difficult = ' '
while difficult not in 'ЛСТ':
    print('Выберите уровень сложности: Л - Легкий, С - Средний, Т - Тяжелый')
    difficult = input().upper()
    if difficult not in 'ЛСТ':
        print('Ваш выбор некорректен.')
    # собственно сама проверка и удаление элементов списка
if difficult == 'С':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficult == 'Т':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ''  # Сюда будем писать некорректные буквы
correctLetters = ''  # Сюда будем записывать корректные буквы
x = getRandomWord(words)  # Выбираем рандомное слово из заданного списка
secretWord = x.lower() #слово из файла приводим в нижний регистр
gameIsDone = False  # Флаг окончания игры. False - игра не завершена

while True:
    # Вызовем функцию отрисовки человечка и прочей информации
    displayBoard(missedLetters, correctLetters, secretWord)

    # После отрисовки вызываем функцию, в которой позволяем игроку ввести букву
    # missedLetters + correctLetters - слепляются два списка и передаются в функцию
    letter = getGuess(missedLetters + correctLetters)

    if letter in secretWord:
        correctLetters = correctLetters + letter

        # Проверяет, выиграл ли игрок.
        foundAllLetters = True  # Предполагаем, что все буквы найдены
        for i in range(len(secretWord)):  # количество итераций цикла зависит от количества букв в загаданном слове
            if secretWord[i] not in correctLetters:  # если буква из загаданного слова не содержится в списке
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Да! Секретное слово - "' + secretWord + '"! Вы угадали!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + letter

        # Проверяет, превысил ли игрок лимит попыток и проиграл.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Вы исчерпали все попытки!\nНе угадано букв: ' + str(len(missedLetters)) + ' и угадано букв: ' + str(
                len(correctLetters)) + '. Было загадано слово "' + secretWord + '".')
            gameIsDone = True

    # Запрашивает, хочет ли игрок сыграть заново (только если игра завершена).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
