
# Управляющие последовательностью
print('Давайте попрактикуемся!')
print('Вы должны знать об управляющий последовательностях с символом \\, которые \n управляет переносом строк и \t отступами')


#Выводит много строчный текст
poem = """
\tДля счастья
мне совсем немного надо.
Хочу тебя \nя нежно обнимать,
Хочу всегда
я быть с тобою рядом
\n\t\tИ никогда не отпускать
"""

print(20*'_')
print(poem)
print(20*'_')


#Выводит математическое действие
five = 10-2 + 3-6
print('Здесь должна быть пятерка: %s' % five)

#Функция и работа с ней
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	
start_point = 10000
beans, jars, crates = secret_formula(start_point)

print('Начиная с: %d' % start_point)
print('У нас есть %d бобов, %d банок и %d ящиков' % secret_formula(start_point))

start_point /= 10

print('Также можно поступить следующим образом: ')
print('У нас есть %d бобов, %d банок и %d ящиков' % secret_formula(start_point))