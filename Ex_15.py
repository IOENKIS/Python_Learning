# Импортируем атрибут argv
from sys import argv

#Присваиваем переменным аргументы
script, filename = argv

#Открываем файл который был введен как аргумент
txt = open('Ex_15/%s' % filename)

print('Содержимое файла %s\n' % filename)

#Выводим то что находится в файле
print(txt.read())
txt.close()

print('Введите имя файла снова: ')
file_again = input('> ')

#Открываем файл еще раз
txt_again = open('Ex_15/%s' % file_again)

#Выводим информацию с файла
print(txt_again.read())
txt_again.close()