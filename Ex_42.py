# Animal наследует object
class Animal(object):
	pass

# Dog наследует Animal
class Dog(Animal):
	def __init__(self, name):
		# 
		self.name = name

#Cat наследует Animal
class Cat(Animal):
	def __init__(self, name):
		#
		self.name = name

#Person наследует object
class Person(object):
	def __init__(self, name):
		#
		self.name = name
		
	# Person - композиция животного некоторого вида
	self.pet = None
		
#Employee наследует Person
class Employee(Person):
	def __init__(self, name, salary):
		# Инициализируем функцию с родительского класса. Хмм, что за страння магия?
		super(Employee, self).__init__(name)
		#
		self.salary = salary

# Fish наследует object
class Fish(object):
	pass

# Salmon наследует Fish
class Salmon(Fish):
	pass

#Halibut наследует Fish
class Halibut(Fish):
	pass

# Создается экземпляр класса Dog с именем 'Rover' и присваивается переменной rover
rover = Dog('Rover')

# Создается экземпляр класса Cat с именем 'Satan' и присваивается переменной satan
satan = Cat('Satan')

# Создается экземпляр класса Person с именем 'Mary' и присваивается переменной mary
mary = Person('Mary')

# У экземпляра mary класса Person устанавливается атрибут pet в значение satan. Таким образом, объект satan (экземпляр класса Cat) становится питомцем объекта mary (экземпляр класса Person).
mary.pet = satan

# Создается экземпляр класса Employee с именем "Frank" и зарплатой 120000, и присваивается переменной frank.
frank = Employee('Frank', 120000)

# У экземпляра frank класса Employee устанавливается атрибут pet в значение rover. Таким образом, объект rover (экземпляр класса Dog) становится питомцем объекта frank (экземпляр класса Employee).
frank.pet = rover

# Создается экземпляр класса Fish и присваивается переменной flipper
flipper = Fish()

# Создается экземпляр класса Salmon и присваивается переменной crouse
crouse = Salmon()

# Создается экземпляр класса Fish и присваивается переменной harry
harry = Halibut()















