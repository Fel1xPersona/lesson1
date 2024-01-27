# list-списки
# name1="Akniet"
# name2="Aknie"
# name4="Akn"
# print(name1,name2,name4)


# names = ["Akniet","Aknie","Akni","Akn"]
# print(names)


# numbers = [10, 20, 30, 40, 50]
# print(numbers)


# ist = [25, 1.5, "Geeks", True]
# print(ist)


# it_company = ["Google", "Meta", "Amazon", "Codex", "Tesla"]
# print(it_company[1:0])


# # # Срезы списков
# print(it_company[1:4:2])   
# print(it_company[::-1])


# # #изменения списков
# it_company[2] = "Codex KG"
# print(it_company)


# it_company.append("Geeks")
# print(it_company)


# it_company.insert(0, "Test")
# print(it_company)


# it_company.pop(0)
# print(it_company)



# Tuple - кортежи
# cars = ["BMW", "Lexus", "Toyota","Honda"]
# print(cars)
# print(type(cars))
# print(cars.count("BMW"))
# print(cars.index("Honda"))

# list_cars = list(cars)
# print(list_cars)
# list_cars.append("Zeekr")
# print(list_cars)

# cars=tuple(list_cars)
# print(cars)

# import random

# random_number = random.randint(1, 3)
# # print(random_number)
# user_number = int(input("Введите цифру от 1 до 3: "))
# if random_number == user_number:
#     print("Поздравляем вы выиграли!")
# else:
#     print("К сожалению вы проиграли случайная цифра:",random_number)

# students = ["Nurbolot", "islam","azatbek", "Akniet","Suimyk"]
# print(random.choice(students))

# задача1
# company = ["BMW", "MERS", "Lexus", "Toyota", "Honda", "Kill-Bill", "Bloody-Marry", "Crocko-Lako", "Denzel-W", "Hey-Jude", "Osh", "Bishkek", "Talas", "New-Yourk", "Moscow"]
# print(company[2:7])


# numbers_list = [1,2,3,4,5]
# reversed_list = list(reversed(numbers_list))
# print(reversed_list)

# a = [1,3,4,5]
# b = [4,5,6,7]
# c = set(a+b)
# print(c)


# numbers_list = [1,2,3,4,5]
# print(min(numbers_list))


# numbers_list = [1,2,3,4,5]
# numbers_list.clear()
# print(numbers_list)


# numbers_list = [1,2,3,4,5]
# print(sum(numbers_list))




# numbers_list = [1,2,3,4,5]
# numbers_list_sum = sum(numbers_list)
# print(numbers_list_sum//len(numbers_list))


# music =["Kill-Bill", "Bloody-Marry", "Crocko-Lako", "Denzel-W", "Hey-Jude",' Good Vibration','Johnny B. Goode	',	'Hey Jude'	,'Smells Like, Teen Spirit', "Привет"]
# music[4], music[8] = music[8], music[4]
# print(music)

# numbers =[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
# 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
# 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
# 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
# 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97,
# 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
# 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128,
# 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143,
# 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158,
# 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173,
# 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188,
# 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
# 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215,
# 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230,
# 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245,
# 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260,
# 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
# 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290,
# 291, 292, 293, 294, 295, 296, 297, 298, 299, 110, 111, 112, 113, 114, 115,
# 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130,
# 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145,
# 146, 147, 148, 149, 150, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259,
# 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274,
# 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289,
# 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 110]
# print(numbers.count(110))


# it_company = ('Google', 'Amazon', 'Microsoft')
# list_it_company =list(it_company)
# list_it_company.append("Google-Play")
# print(list_it_company)
# list_it_company1 =tuple(list_it_company)
# print(list_it_company1)
# задача 11
# print(it_company[1]) 
# задача12
# list_it_company =list(it_company)
# list_it_company [0] = "Apple"
# print(list_it_company)
# задача 13
# print(it_company[0::2])

# задача 14

# text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language',
# 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean',
# 'syntax', 'and', 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite',
# 'with', 'our', 'Python', '3', 'overview')
# print(text_tuple.count("Python"))

# задача 15
# password = input("Введите пароль: ")
# password_check =input("Подтвердите пароль: ")
# if len(password) < 8:
#     print('Короткий пароль')
# elif password == "123":
#     print("Простой пароль")
# elif password != password_check:
#     print("Различаются")
# elif password == password_check:
#     print("Успешно создан пароль")
# else:
#     print("Ошибка")




