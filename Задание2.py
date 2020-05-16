''' Задание 2.
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
'''

seconds_input = input("Пожалуйста введите количество секунд для пересчёта: ")
hours = int(seconds_input) // 3600
minutes = (int(seconds_input) % 3600) // 60
seconds = int(seconds_input) % 60

print(hours)
print(minutes)
print(seconds)



# Нужно доделать вывод в правильном виде.