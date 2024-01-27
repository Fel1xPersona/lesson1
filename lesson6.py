# Исключения try, except
# try:
#     print(100/ 2)
# except ZeroDivisionError:
#     print("Деление на ноль невозможно")


# try:
#     name = "Akniet"
#     print(name1)
# except NameError:
# #     print("Обработали ошибку")

# while True:   
#     try:
#         num1  =int(input("Введите первое число: "))
#         num2  =int(input("Введите второе число: "))
#         Operator = input("Знак(+,-,*,/,%): ")
#         if Operator == '+' :
#             print(num1+num2)
#         elif Operator == '-' :
#             print(num1-num2)
#         elif Operator == "*" :
#             print(num1*num2)
#         elif Operator == "/" :
#             print(num1/num2)
#         elif Operator == "%":
#             try:
#                 print(num1%num2)
#             except ZeroDivisionError:
#                 print("Делить на ноль нельзя!")
#         else:
#             print("Ошибка")
#             break
#     except ValueError:
#         print("Введите число!")

# raise ValueError("Мы сами вызвали данную ошибку")

# Тип данных set
# numbers1  = [1, 2, 3, 4, 5,]
# numbers2 = [3, 4, 5, 6, 7]
# print(numbers1 + numbers2)
# print(set(numbers1 + numbers2))

# names = {"Islam", "Syimyk", "Timur", "Nurbolot", "Islam", "Timur"}
# print(names)

# st = {True, "Geeks", 10, 30.1, (10, 20, 30)}
# print(st)

# cars = {"BMW","lexus", "Mers", "Zeekr", "Toyota", "BMW"}
# print(cars)
# cars.add("Tesla")
# print(cars)
# cars.remove("Zeekr")
# print(cars)
# print(cars[0])
# cars.pop()
# print(cars)

# Тип данных frozenset
# frzn_set =  frozenset({10, 20, 30, 40, 50, 10, 20})
# print(frzn_set)
# print(type(frzn_set))


# # Тип данных dictionary - словарь
student = {"name":"Nurbolot", "age":19}
print(student.values())
print(student)

student.setdefault('language', 'Python')
print(student)

print(student['name']) #У словарей нету индексов но есть ключи
print(student['language'])
student.pop('age')
print(student)

student['language'] = "Javascript"
print(student)
geeks = {'title':'Geeks', 'count_students':412, 'count_employees':20}
print(geeks)
print(geeks.keys())