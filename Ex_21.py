def add(a, b):
	print('СЛОЖЕНИЕ %d + %d' % (a, b))
	return a + b

def subtract(a, b):
	print('ВЫЧИТАНИЕ %d - %d' % (a, b))
	return a - b

def multiply(a, b):
	print('УМНОЖЕНИЕ %d * %d' % (a, b))
	return a * b

def divide(a, b):
	print('ДЕЛЕНИЕ %d / %d' % (a, b))
	return a / b 

print('Давайте выполним несколько вычилений с помощью функций!')

age = add(30, 7)
height = subtract(190, 4)
weight = multiply(35, 2)
iq = divide(220, 2)

print('Возраст: %d, Рост: %d, Вес: %d, IQ: %d' % (age, height, weight, iq))

print('Это головоломка')

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print('Получаеться %d. Вы можете это вычислить вручную?' % what)