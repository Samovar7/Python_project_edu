'''
name = 'Alex'
age = None
a = 42
print(id(a))
a = 'Hello world'
print(id(a))
print(name, age, a, 456, 'text', sep=' (=^.^=) ', end='\n')
print('Any text')
res = input('Print your text: ')
print('Ты написал: ', res)


color = input('Твой любимый цвет: ')
match color:
    case 'red' | 'orange':
        print('Любитель яркого')
    case 'green':
        print('Ты не охотник?')
    case 'blue':
        print('Ха, классика!')
    case _:
        print('Тебя не понять')
'''

data = [0,1,2,3,4,5,6,7,8,9]
for i in range(15):
    print(i, end=' | ')