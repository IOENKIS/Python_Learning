people = int(input('Введи количество людей\t'))
cars = int(input('Введи количество машин\t'))
buses = int(input('Введи количество автобусов\t'))

if cars > people:
	print('Поедем на машине')
elif cars < people:
	print('Не поедем на машине')
else:
	print('Мы не можем выбрать')

if buses > cars:
	print('Слишком много автобусов')
elif buses < cars:
	print('Может, поехать на автобусе?')
else:
	print('Мы до сих пор не можем выбрать')
	
if people > buses:
	print('Хорошо, давайте поедем на автобусе')
else:
	print('Прекрасно, давайте останемся дома')