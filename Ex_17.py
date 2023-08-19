#Импортируем атрибут argv с библиотеки sys и так же exists с библиотеки os.path что бы проверить существует ли файл
from sys import argv
from os.path import exists

#Делаем аргументы при запуске скрипта
script, from_file, to_file = argv

print('Копирование данных из файла %s в файл %s' % (from_file, to_file))

#Открывает и сразу читаем первый файл
indata = open(from_file).read()

#Проверяем его длину
print('Исходный файл имеет размер %d байт' % len(indata))

#Проверяем существует ли файл в который нужно копировать информацию
print('Файл назначения существет? %r' % exists(to_file))
print('Готов к работе, нажмите клавишу Enter для продожения или CTRK+C (^C) для отмены')

input('?')

#Открываем второй файл и записываем в него информацию с первого
out_file = open(to_file, 'w')
out_file.write(indata)

print('Отлично, все сделано...')

#Закрываем оба файла 
out_file.close()



