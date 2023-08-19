import random
from urllib.request import urlopen
import sys

WORD_URL = 'http://learncodethehardway.org/words.txt'
WORDS = []

PHRASES = {
	'class %%%(%%%):':
	'Созаеться класс с именем %%%, наследующим %%%',
	'class %%%(object):\n\tdef __init__ (self, ***) ':
	'Класс %%% комбинирует __init__ с параметрами self, ***', 
	'class %%%(object):\n\tdef *** (self, @@@)':
	'Класс %%% комбинирует функцию с именем *** с параметрами self, @@@',
	'*** = %%%() ':
	'Создаеться *** как экземпляр класса %%%', 
	'***.***(@@@) ':
	'Из *** получаеться функция ***, а затем вызываеться с параметрами self, @@@', 
	'***.*** = \'***\'':
	'Из *** получаеться атрибут ***, а затем устанавливаеться равным \'***\''

}

# Тренировка запоминания фраз
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == 'russian':
	PHRASE_FIRST = True

# Подгружаем слова с сервера
for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip().decode('utf-8'))

def convert(snippet, phrase):
	class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count('%%%'))]
	other_names = random.sample(WORDS, snippet.count('***'))
	results = []
	param_names = []
	
	for i in range(0, snippet.count('@@@')):
		param_count = random.randint(1, 3)
		param_names.append(', '.join(random.sample(WORDS, param_count)))
	
	for sentence in snippet, phrase:
		result = sentence[:]
	
		# Вымышленные имена классов
		for word in class_names:
			result = result.replace('%%%', word, 1)
	
		# Вымышленные прочие имена
		for word in other_names:
			result = result.replace('***', word, 1)
		
		# Список вымышленных параметров
		for word in param_names:
			result = result.replace('@@@', word, 1)
	
		results.append(result)
		
	return results
	
# выполнение пока не нажато сочетание клавиш CTRL+Z
try:
	while True:
		snippets = list(PHRASES.keys())
		random.shuffle(snippets)
		
		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question
			
			print(question)
			
			input('> ')
			print('ОТВЕТ: %s\n\n' % answer)
except EOFError:
	print('\nПока!')
	
	
	
	
	
	
	
	
	
	
	
	
	