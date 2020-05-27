'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

'''

import random
import re

text1 = open("Задание5.txt", 'w')

length_list = random.randint(5,20)
length_number = random.randint(0,500)


ready_list = []
size = len(ready_list)
offset = 0
chunk = 100

while True:
    if len(ready_list) == length_list:
        break

    else:
        number = str(random.randint(0,length_number))
        ready_list.append(number)
        text1.write(number + ' ')

text1.close()

text1 = open("Задание5.txt", 'rt')
a = text1.read()

print(a)


'''t = []
n = 0
for line in a:

    replaced = re.findall(r'\d+', line)
    t.append(int(replaced))'''
x=0
numbers = [int(x) for line in a]

print(numbers)


s = sum(list(t))


