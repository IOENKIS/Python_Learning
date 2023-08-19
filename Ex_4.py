# Объявляем переменные
cars = 100
space_in_a_car = 4
drivers = 30
passangers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capasity = cars_driven * space_in_a_car
average_passengers_per_car = passangers / cars_driven

# Выводим переменные
print(f'В наличии {cars} автомобилей')
print(f'И только {drivers} водителей вышли на работу')
print(f'Получаеться, что {cars_not_driven} машин пустуют')
print(f'Мы можем перевести сегодня {carpool_capasity} человек')
print(f'Сегодня нужно отвести {passangers} человек')
print(f'В каждой машине будет примерно {average_passengers_per_car} человека')