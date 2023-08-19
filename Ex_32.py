the_count = [1, 2, 3, 4, 5]
fruits = ['яблоко', 'апельсин' , 'персик', 'абрикос']
change = [1, '25', 2, '50', 3, '75']

# Цикл for первого типа обрабатывает список
for number in the_count:
	print('Счетчик %d' % number)

# То же, что и выше
for fruit in fruits:
	print('Фрукт: %s' % fruit)

# Так же можно обрабатывать смешанные списки
# Используется оператор %r, так как неизвестен тип значения
for i in change:
	print('Я получил %r' % i)

# Так же мы можем создавать списки, начнем с пустого 
elements = []

# Затем используется функция range для ограничения диапазона
for i in range(0, 6):
	print('Добавление %d в список' % i)
	# append - функция для добавления элементов и списков
	elements.append(i)

# Теперь мы их выводим
for i in elements:
	print('Номер эелемента: %d' % i)