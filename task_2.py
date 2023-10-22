'''
a = 5
print(type(a))
a = "hello world"
print(type(a))
a = 42.0 * 3.141592 / 2.71828
print(type(a))

a = 5
print(type(a), id(a))
a = "hello world"
print(type(a), id(a))
a = 42.0 * 3.141592 / 2.71828
print(type(a), id(a))


data = 42
print(isinstance(data, int))
data = True
print(isinstance(data, int))
data = 3.14
print(isinstance(data, (int, float, complex)))


num = 2 + 2 * 2
digit = 36 / 6
print(num == digit)
print(num is digit)

num = 2 + 2 * 2
digit = 36 // 6
print(num == digit)
print(num is digit)


a = 5
print(a, id(a))
a += 1
print(a, id(a))
txt = 'Hello world!'
txt[5] = '_'

txt = 'Hello world!'
print(txt, id(txt))
txt = txt.replace(' ', '_')
print(txt, id(txt))

a = c = 2
b = 3
print(a, id(a), b, id(b), c, id(c))
a = b + c
print(a, id(a), b, id(b), c, id(c))

x = 200
y = 'text'
z = 3.1415
print(hash(x), hash(y), hash(z))
my_list = [x, y, z]
print(hash(my_list)) # получим ошибку, т.к. list изменяемый
'''
'''
text = input('Введите любой текст: ')
print(type(text))
print(isinstance(text, str))
print(id(text))
print(hash(text))

print("Hello world!".__doc__)
print(str.__doc__)

print("Hello world!".upper())
print("Hello world!".count('o'))
print(dir("Hello world!"))
#help(str)
'''
import sys
'''
STEP = 2 ** 16
num = 1
for _ in range(30):
    print(sys.getsizeof(num), num)
    num *= STEP

num = 2 ** 16 - 1
b = bin(num)
o = oct(num)
17
h = hex(num)
print(num, b, o, h)

DEFAULT = 42
num = int(input('Введите уровень или ноль для значения по умолчанию: '))
level = num or DEFAULT
print(level)

name = input('Как вас зовут? ')
if name:
    print('Привет, ' + name)
else:
    print('Анонимус, приветствую')

data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
while data:
    print(data.pop())

LIMIT = 120
ATTENTION = 'Внимание!'
name = input('Твоё имя? ')
age = int(input('Твой возраст? '))
text = ATTENTION + ' Хоть тебе и осталось ' + str(100 - age) +\
" до ста лет, но длинна строки не должна превышать " + str(LIMIT) + ' символов.'
print(text)


empty_str = ''
en_str = 'Text'
ru_str = 'Текст'
unicode_str = '😀😍😉🙃'
print(empty_str.__sizeof__())
print(en_str.__sizeof__())
print(ru_str.__sizeof__())
print(unicode_str.__sizeof__())
'''
import math
import decimal
import fractions
'''
print(math.pi, math.e, math.inf, math.nan, math.tau, sep='\n')
print(1/3)

pi = decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375')
print(pi)
num = decimal.Decimal(1) / decimal.Decimal(3)
print(num)
print()

decimal.getcontext().prec = 120
science = 2 * pi * decimal.Decimal(23.452346) ** 2
print(science)
'''

f1 = fractions.Fraction(1, 3)
print(f1)
f2 = fractions.Fraction(3, 5)
print(f2)
print(f1 * f2)

a = complex(2, 3)
b = complex('2+3j')
print(a, b, a == b, sep='\n')
print(type((5,3)))
