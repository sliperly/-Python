'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.

'''




f = open("Задание2.txt", "r", encoding = "utf-8")
p = len(f.readlines())
print(p)



with open("Задание2.txt") as f:
    for line in f:
        print(len(line.split()))

f.close()