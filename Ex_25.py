def break_words(stuff):
	'''Эта функция разбирает текст на слова'''
	words = stuff.split(' ')
	return words

def sort_words(words):
	'''Сортирует слова'''
	return sorted(words)

def print_first_word(words):
	'''Выводит первое слово после извлечения'''
	print(words.pop(0))

def print_last_word(words):
	'''Выводит последнее слово после извлечения'''
	print(words.pop(-1))

def sort_sentence(sentence):
	'''Принимает целое предложение и возвращает отсортированные слова'''
	return sort_words(break_words(sentence))

def print_first_and_last(sentence):
	'''Выводит первое и последнее слова предложения'''
	print_first_word(break_words(sentence))
	print_last_word(break_words(sentence))

def print_first_and_last_sorted(sentence):
	'''Сортирует слова, а затем выводит первое и последнее'''
	print_first_word(sort_sentence(sentence))
	print_last_word(sort_sentence(sentence))
	