def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print('У нас есть %d бутылок лимонада!\nУ нас есть %d коробок чипсов!\nЭтого достаточно для вечеринки!\nПоехали!\n' % (cheese_count, boxes_of_crackers))

print('Мы можем непосредственно передать числа функции: ')
cheese_and_crackers(20, 30)

print('ИЛИ, мы можем использовать переменные нашего сценария: ')
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print('Мы даже можем выполнять вычисления внутри фунции: ')
cheese_and_crackers(10 + 20, 5 + 6)

print('И объединять переменный с вычислениями: ')
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print('Теперь я у тебя спрошу количество лимонада и чипсов:')
a_cheese = int(input('>'))
a_crackers = int(input('>'))
cheese_and_crackers(a_cheese, a_crackers)