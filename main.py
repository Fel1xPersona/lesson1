while True:   
    num1  =int(input("Введите первое число: "))
    num2  =int(input("Введите второе число: "))
    s = input("Знак(+,-,*,/,%): ")
    if s == '+' :
        print(num1+num2)
    elif s == '-' :
        print(num1-num2)
    elif s == "*" :
        print(num1*num2)
    elif s == "/" :
        print(num1/num2)
    elif s == "%":
        print(num1%num2)
    else:
        print("Ошибка")
        break