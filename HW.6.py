# Исключения в программировании-это механизм,который позволяет программе обрабатывать нетипичную ситуацию и приекращать работу.Благодоря этому механизму разработчик может описать в коде реакцию программы на такие с этом не притуации
 

#  numbers1  = [1, 2, 3, 4,]
# numbers2 = [3, 4, 5,]
# print(numbers1 + numbers2)
# print(set(numbers1 + numbers2))

# while True:
#    try:
#       num1 = int(input("Введите первое число: "))
#       num2 = int(input("Введите второе число: "))
#       print('+','-','*','/' )
#       operator = input('Выберите действие:')
        
#       if operator == '+':
#          result1 = (num1 + num2)
#          print(f"Сумма: {result1}")
#          if result1 % 2==0:
#             print("Четное: ")
#          else:
#             print("Нечетное: ")

#       elif operator == '-':
#          result2= (num1 - num2)
#          print(f"Вычетание: {result2}")
#          if result2 % 2==0:
#             print("Четное: ")
#          else:
#             print("Нечетное: ")

#       elif operator == '*':
#          result3 = (num1 * 2)
#          print(f"Умножение: {result3}")
#          if result3 % 2==0:
#             print("Четное: ")
#          else:
#             print("Нечетное: ")

#       elif operator == '/':
#          result4 = (num1 / num2)
#          try:
#             print(f"Деление: {result4}")
#             if result4 % 2==0:
#                print("Четное: ")
#             else:
#                print("Нечетное: ")
#          except ZeroDivisionError:
#             print("Деление на ноль не возможно")

#    except ValueError:
#       print("Ошибка: введите числа заново")
#    #  except ZeroDivisionError:
   #      print("Деление на ноль не возможно")


# dictionary_1 = {'a': 300, 'b': 400}
# dictionary_2 = {'c': 500, 'd': 600}
# dictionary_1.update(dictionary_2)
# print ("обновление словаря : ", dictionary_1)

# numbers = {"num_1" : 1, "num_2" : 2, "num_3" :3, "num_100" : 100}
# 


# student = {'name' : 'Askhat', 'age' : 17}
# student['age'] =17*2
# # print(student)


# student = {'name' :'Askhat' , 'age' :17, 'color' : 'White'}
# student['age']=16
# print(student)


# # student = {'name' : 'Askhat', 'age' : 17}
# # student.pop("age")
# # print(student)

# student = {'name':'Askhat'}
# student.setdefault('address', 'Западный анар')
# print(student)


# def  izogramma(word:str="Geeks")-> bool:
#    #  print(word)
#    print(len(set(word)))
#    if len(set(word.lower())) ==len(word.lower()):
#          print(True)
#    else:
#         print(False)
# izogramma("Telegram")
# izogramma("IT")
# izogramma("BMW")
# izogramma("telEgram")


def it_geeks():
    return "Geeks Osh IT"
it_geeks()


