# Импорт библиотек
import turtle
import random # Библиотека для работы со случайными значениями
import time # Ббилиотека для работы с таймингами

# Глобальные переменные (Негативная практика с точки зрения организации функций)
sc = None
t1 = None # Объект библиотеки Turtle
t2 = None
win = False

# Функция базовой настройки
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
    
def start_race():
    global win 
    for i in range(100):
        if not win:
            t1.forward(random.randint)
            t1.forward(random.randint)
            check_winner()
        else:
            break

def check_winner():
    global win
    if t1.xcor()>150:
        print('Победила красная черепашка')
        win = True
    if t2.xcor()>150:
        print('Победила зелёная черепашка')
        win = True

setup()

start_race()
