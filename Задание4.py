'''
Задание 4.
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''

number = int(input("Введите пожалуйста какое-нибудь целое положительное число: "))

i = number
number1 = 0
number2 = 0
biggest_number = 0


if number <= 0:
    print("В следующий раз попробуйте ввести положительное число")
else:
    while i != 0:
        i = number
        number1 = number % 10
        number = number // 10
        number2 = number % 10
        number = number // 10
        if number1 > number2 and number1 > biggest_number:
            biggest_number = number1
        elif number2 > biggest_number:
            biggest_number = number2
    print(biggest_number)