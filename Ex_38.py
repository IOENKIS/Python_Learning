ten_things = 'Apples Oranges Crows Telephone Light Sugar'

print('Погодите, тут меньше 10 объектов. Давайте исправим это')

stuff = ten_things.split(' ')
more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print('Добавляем: ', next_one)
	stuff.append(next_one)
	print('теперь у нас %d объектов' % len(stuff))

print('Итак: ', stuff)

print('Давайте кое-что сделаем с нашими объектами')

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))

























