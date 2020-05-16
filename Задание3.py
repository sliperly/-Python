# !
''' Задание 3.
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''

number = input("Пожалуйста, введите какое-нибудь число N: ")
N = int(number)
NN = int(number + number)
NNN = int(number + number + number)
summa = N + NN + NNN
print("А Вы знаете, что если сложить N + NN + NNN, то получится: " + str(summa))

