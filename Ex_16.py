from sys import argv

script, filename = argv

print('Я собираюсь стереть файл %r' % filename)
print('Если вы не хотите стирать его, нажмите сочетание клавиш CTRL+C (^C)\n')
print('Если вы хотите стереть файл, нажмите клавишу Enter\n')

input('?')

print('Открытие файла...')
target = open(filename, 'w')

print('Очистка файла. До свидания!')
target.truncate()

print('Теперь я запрашиваю у вам три строки\n')
line1 = input('Cтрока 1: ')
line2 = input('Cтрока 2: ')
line3 = input('Cтрока 3: ')

print('Это я запишу в файл')

target.write(line1 + '\n' + line2 + '\n' + line3 + 
'\n')

print('И наконец, я закрою файл')
target.close()

print('А теперь давайте прочитаем что вы там написали\n')
target = open(filename)

print(target.read())

print('\nЭто всё. Я закрываю файл')
target.close()