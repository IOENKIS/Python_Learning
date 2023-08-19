from sys import argv

script, user_name = argv
prompt = '* '

print('Привет %s, Я - сценарий %r' % (user_name, script))
print('Я хочу задать тебе несколько вопросов')
print('Я тебе нравлюсь, %s' % user_name)
likes = input(prompt)
print('Где ты живешь, %s' % user_name)
lives = input(prompt)
print('на каком компьютере ты работаешь?')
computer = input(prompt)
print('''
Итак, ты ответил %r на вопрос, нравлюсь ли я тебе. 
Ты живешь в %r. Не представляю, где это.
И у тебя есть компьютер %r. Прекрасно!'''  % (likes, lives, computer))