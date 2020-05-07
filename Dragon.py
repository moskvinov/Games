import random
import time

#Функция, которая выводит вступительное интро
def Intro():
    print('''    Вы находитесь в землях, заселенных драконами.
    Перед собой вы видите две пещеры. В одной из них — дружелюбный дракон,
    который готов поделиться с вами своими сокровищами. Во второй —
    жадный и голодный дракон, который мигом вас съест.''')
    print()

#Функция, в которой мы делаем выбор пещеры. Этот номер пещеры она возвращает в основное тело программы.
def choose_cavern():
    cave = ''
    while cave != '1' and cave != '2':
        print('В какую пещеру вы войдете? (нажмите клавишу 1 или 2)')
        cave = input()

    return cave

def check_cavern(cavern_number):
    #держим игрока в напряжении
    print('Вы приближаетесь к пещере...')
    time.sleep(2) #тут задается сколько ждать, перед тем как вывести следующую строку. В данном случае программа спит 2 секунды, потом выводит следующий принт
    print('Ее темнота заставляет вас дрожать от страха...')
    time.sleep(2)
    print('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...')
    print()
    time.sleep(2)
    #рандомом выбираем, хочет ли нас дракон съесть или нет
    dragon_choose = random.randint(1, 2)

    if cavern_number == str(dragon_choose):
        print('...делится с вами своими сокровищами!')
    else:
        print('...моментально вас съедает!')

#Функция, которая принимает и анализирует ответ пользователя об окончании или продолжении игры
def game_over ():
    user_choose = input()
    if user_choose == 'да' or user_choose == 'Да' or user_choose == 'д' or user_choose == 'Д' or user_choose == 'lf' or user_choose == 'Lf' or user_choose == 'Yes'  or user_choose == 'yes':
        user_choose = 'Да'
    elif user_choose == 'нет' or user_choose == 'Нет' or user_choose == 'н' or user_choose == 'Н' or user_choose == 'ytn' or user_choose == 'Ytn' or user_choose == 'No'  or user_choose == 'no':
        user_choose = 'Нет'
        print('Спасибо за игру. Хорошего дня!')
    else:
        user_choose = 'Нет'
        print('К сожалению, я не могу распознать Ваш выбор. Игра будет завершена. Буду ждать Вашего возвращения')
    return user_choose

#тело программы
play_again = 'Да'
while play_again == 'Да':
    Intro() #выводим стартовое интро
    cavern_number = choose_cavern() # Вызываем функцию, в которой выбираем номер пещеры. Функция возвращает номер пещеры и
                                    # записывает значение в переменную cavern_number
    check_cavern(cavern_number) #вызываем функцию проверки, правильную ли пещеру мы выбрали
    print('Попытаете удачу еще раз? (Да/Yes или Нет/No)') #после того как мы выиграли или проиграли, спрашиваем пользователя о новой попытке.
    play_again = game_over()