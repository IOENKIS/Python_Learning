from sys import exit

def gold_room():
	print('Здесь полно золота. Сколько кг ты унесешь?')
	
	next = input('> ').lower()
	if not next.isdigit():
		dead('Эй, ввести надо чилсло!')
	
	if next < '50':
		print('Шикарно! Ты не жадный, по этому выигрываешь!')
		exit(0)
	else:
		dead('Ах ты жадина!')


def bear_room():
	print('Здесь сидит медведь')
	print('У медведя бочка с медом')
	print('Медведь закрыл собой дверь выхода')
	print('Как переместить медведя?\nОтобрать мед или подразнить медведя?')
	bear_moved = False
	
	while True:
		next = input('> ').lower()
		
		if next == 'отобрать мед':
			dead('Медведь посмотрел на тебя и ударил лапой по лицу')
		elif next == 'подразнить медведя' and not bear_moved:
			print('Медведь отошел от двери. Вы можете войти в нее. Подразнить медведя или войти в дверь?')
			bear_moved = True
		elif next == 'подразнить медведя' and bear_moved:
			dead('Медведь разозлился и откусил тебе ногу')
		elif next == 'войти в дверь' and bear_moved:
			gold_room()
		else:
			print('Понятия не имею что происходит')

def cthulhu_room():
	print('На вас смотрит великий и ужасный Ктулху')
	print('Он смотрит на тебя и ты начинаешь сходить с ума')
	print('Убежать или съесть свою голову?')
	
	next = input('> ').lower()
	
	if 'убежать' in next:
		start()
	elif 'съесть свою голову' in next:
		dead('Хм, а это даже и вкусно!')
	else:
		cthulhu_room()
		
def dead(why):
	print(why, 'Великолепно!')
	exit(0)
		
def start():
	print('Ты в темной комнате')
	print('Отсюда ведут только две двери, налево и направо')
	print('Куда ты повернешь?')
	
	next = input('> ').lower()
	
	if next == 'налево':
		bear_room()
	if next == 'направо':
		cthulhu_room()
	else:
		dead('Ты ходишь из комнаты в комнату, пока не умираешь с голоду')
		

start()
		
		
		
		
		
		
		
		
		
		
	