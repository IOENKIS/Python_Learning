i = 0
numbers = []

while i < 6:
	print('Вверху значение i равно %d' % i)
	numbers.append(i)
	
	i += 1
	print('Текущие значение: ', numbers)
	print('Внизу значение i равно %d' % i)

print('Значения: ', end = ' ')
for i in numbers:
	print(i)