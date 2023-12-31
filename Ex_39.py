# Схема связей аббревиатур с названиями стран
countries = {
	'Украина': 'UA',
	'Германия': 'DE',
	'Узбекистан': 'UZ',
	'Зимбабве': 'ZW',
	'Турция': 'TR'
}

# Создание базового набора стран и некоторых городов в них
cities = {
	'UZ': 'Газли',
	'TR': 'Сарыгерме',
	'DE': 'Мюнхен'
}

# Добавление некоторых городов
cities['ZW'] = 'Гверу'
cities['UA'] = 'Киев'

# Вывод некоторых городов
print('- ' * 10)
print('В стране ZW есть город: ', cities['ZW'])
print('В стране UA есть город: ', cities['UA'])

# Вывод некоторых стран
print('- ' * 10)
print('Аббривеатура Турции: ', countries['Турция'])
print('Аббривеатура Германии: ', countries['Германия'])

# Выполняется с учетом страны и словаря городов
print('- ' * 10)
print('В Турции есть город', cities[countries['Турция']])
print('В Германии есть город', cities[countries['Германия']])

# Вывод аббревиатур всех стран
print('- ' * 10)
for i, j in countries.items():
	print('%s имеет аббревиатуру %s' % (i, j))

# Вывод всех городов в странах
print('- ' * 10)
for i, j in cities.items():
	print('В стране %s есть город %s' % (i, j))

# А теперь сразу оба типа данных
print('- ' * 10)
for i, j in countries.items():
	print('В стране %s используется аббревиатура %s и есть город %s' % (i, j, cities[j]))

# Безопасное получение аббревиатуры страны, которая не представлена
print('- ' * 10)
country = countries.get('США', None)

if not country:
	print('Прошу прощения, США не обнаружено')

# Получение города со значением по умолчанию
print('- ' * 10)
city = cities.get('US', 'не существует')
print('В стране \'US\' есть город: ', city)









