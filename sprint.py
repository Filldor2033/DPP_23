import turtle
import random

# Глобальные переменные
'''! Использование глобальных переменных в функциях '''
sc = None
t1 = None
t2 = None
win = False

# Функция базовой настройки
''' Логика настроек программы '''
def setup():
    global sc, t1, t2
    sc = turtle.Screen()
    sc.setup(500,500)
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t1.color('red')
    t2.color('blue')
    t1.shape('turtle')
    t2.shape('turtle')
    t1.penup()
    t1.penup()
    t1.goto(-150,50)
    t2.goto(-150,-50)

# Функция для запуска игры
''' Отсутствие структуры (весь алгоритм написан в функциях, а не классах) '''
def start_race():
    global win 
    for i in range(100):
        if not win:
            t1.forward(random.randint)
            t1.forward(random.randint)
            check_winner()
        else:
            break
# Функция для определения победителя
''' Отсутствие структуры (весь алгоритм написан в функциях, а не классах) '''
def check_winner():
    global win
    if t1.xcor()>150:
        print('Победила красная черепашка')
        win = True
    if t2.xcor()>150:
        print('Победила зелёная черепашка')
        win = True

'''Логика игрового процесса'''
setup()
start_race()


'''! Код невозможно переиспользовать, поскольку он не представляет собой модуль '''
