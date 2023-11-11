'''
my_list = [4, 8, 2, 9, 1, 7, 2]
res = reversed(my_list)
print(type(res), res)
rev_list = list(reversed(my_list))
print(rev_list)

my_list = [4, 8, 2, 9, 1, 7, 2]
my_list.reverse()
print(type(my_list), my_list)
'''
'''
my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
print(my_list[2:7:2])
print(my_list[:7:2])
print(my_list[2::2])
print(my_list[2:7:])
print(my_list[8:3:-1])
print(my_list[3::])
print(my_list[:7:])
'''
'''
my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
new_list = my_list
print(my_list, new_list, sep='\n')
my_list[2] = 555
print(my_list, new_list, sep='\n')

my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
new_list = my_list.copy()
print(my_list, new_list, sep='\n')
my_list[2] = 555
print(my_list, new_list, sep='\n')
'''
'''
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_m = matrix.copy()
print(matrix, new_m, sep='\n')
matrix[0][1] = 555
print(matrix, new_m, sep='\n')
print()

import copy
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_m = copy.deepcopy(matrix)
print(matrix, new_m, sep='\n')
matrix[0][1] = 555
print(matrix, new_m, sep='\n')
'''
'''
my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(len(my_list))
print(len(matrix))
print(len(matrix[1]))
print()
my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
print(my_list[2:6:2])
print(my_list.pop())
print(my_list.extend([314, 42]))
print(my_list.sort(reverse=False))
print(my_list)
'''
'''
text = 'Hello world!'
print(text[6])
print(text[3:7])

new_txt = text.replace('l', 'L', 2)
print(text, new_txt, sep='\n')

text = 'Hello world!'
print(text.count('l'))
print(text.index('l'))
print(text.find('l'))
print(text.find('z'))
'''
'''
name = 'Alex'
age = 12
text = 'Меня зовут {} и мне {} лет'.format(name, age)
print(text)
'''
'''
pi = 3.1415
print(f'Число Пи с точностью два знака: {pi:.2f}')
data = [3254, 4364314532, 43465474, 2342, 462256, 1747]
for item in data:
    print(f'{item:^10}')

num = 2 * pi * data[1]
print(f'{num = :_}')
'''
'''
link = 'https://habr.com/ru/users/dzhoker1/posts/'
urls = link.split('/')
print(urls)
a, b, c = input('Введите 3 числа через пробел: ').split()
print(c, b, a)
print()
a, b, c, *_ = input('Введите 3 числа через пробел: ').split()
print(_)
'''
'''
text = 'однажды в СТУДЁНУЮ зИмнЮЮ ПоРУ'
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

text = 'Однажды в студёную зимнюю пору'
print(text.startswith('Однажды'))
print(text.endswith('зимнюю', 0, -5))

text = 'Привет, мир!'
print(text.find(' '))
print(text.title())
print(text.split())
print(f'{text = :>25}')
'''
'''
my_tuple = (2, 4, 6, 2, 8, 10, 12, 14, 16, 18)
print(my_tuple[2:6:2])
print(my_tuple[-3])
print(my_tuple.count(2))
print(f'{my_tuple = }')
print(my_tuple.index(2, 2))
print(type('text',))
'''
'''
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.get('two'))
print(my_dict.get('five'))
print(my_dict.get('five', 5))
print(my_dict.get('ten', 5))
print(my_dict)
'''
'''
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.setdefault('five')
print(f'{spam = }\t{my_dict=}')
eggs = my_dict.setdefault('six', 6)
print(f'{eggs = }\t{my_dict=}')
new_spam = my_dict.setdefault('two')
print(f'{new_spam=}\t{my_dict=}')
new_eggs = my_dict.setdefault('one', 1_000)
print(f'{new_eggs=}\t{my_dict=}')
'''
'''
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.values())
for value in my_dict.values():
    print(value)
'''
'''
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.popitem()
print(f'{spam = }\t{my_dict=}')
eggs = my_dict.popitem()
print(f'{eggs = }\t{my_dict=}')

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.pop('two')
print(f'{spam = }\t{my_dict=}')
#err = my_dict.pop('six') # KeyError: 'six'
#err = my_dict.pop() # TypeError: pop expected at least 1 argument, got 0
'''

text_en = 'Hello world!'
res = text_en.encode('utf-8')
print(res, type(res))
text_ru = 'Привет, мир!'
res = text_ru.encode('utf-8')
print(res, type(res))
