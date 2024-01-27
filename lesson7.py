# Функции Python
# """Функции Python представляет собой особый участок кода которой можно вызывать обратившись к нему 
# по имени,которым он был назван.Функции можно создать при помощи оператора Python - def"""

# def hello():
#     print("Hello world")
# hello() #вызов функции по имени Hello


# def it_geeks():
#     print("Geeks - айти курсы в Оше")
#     print(10 + 44)
# it_geeks()


# def add():
#     num1 = int(input("Первое число:"))
#     num2 = int(input("Введите второе число:"))
# #     print(num1 + num2)
# add()

# def mult(num1, num2):#num1, num2 - параметры
#     print(num1 + num2)
# mult(10, 40)#10,  40 - это аргументы к функции


# def welcome(names:list) -> str:
#     for name in names:
#         print(f"Здравствуйте{name[0]}.")
# list_names = ["Kurmanbek ","Beksultan", "Islam"]
# welcome(list_names)


# def chet_nechet(number:int=2) -> str:
#     "Функция для вычисления четных и нечетных чисел"
#     if number % 2 == 0:
#       print(number, "четный")
#     else:
#        print(number, "нечетный")
# chet_nechet(100)
# chet_nechet()
# import time
# def chet_time():
#     start_time = time.time()
#     print("Hello world")
#     time.sleep(1)
#     print("Geeks")
#     end_time = time.time()
#     print(end_time - start_time)
# chet_time()

import random

def generate_password():
    letters = "qwertyuiopasdfghjklzxcvbnm"
    random_letter = random.choice(letters)
    print(random_letter)
    result = ""
    for i in range(10):
         random_letter = random.choice(letters)
         result += random_letter
    print(result)
generate_password()