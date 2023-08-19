my_name = 'Иван Киселев'
my_age = 17
my_height = 178 # см
my_weight = 83 # кг
my_eyes = 'Карие'
my_teeth = 'Белые'
my_hair = 'Темно-русые'

print ('Давайте поговорим о человеке по имени %s' % my_name)
print ('Его рост сотсавляет %d дюймов' % round(my_height/2,54))
print ('Он весит %d футов' % round(my_weight/2,20462262185))
print ('У него %s глаза и %s волосы' % (my_eyes, my_hair))
print ('Его зубы обычно %s хотя он и любит пить кофе' % my_teeth)

print ('Если я сложу %d, %d и %d, то получу %d' %(my_age, round(my_height/2,54), round(my_weight/2,20462262185), my_age + round(my_height/2,54) + round(my_weight/2,20462262185)))