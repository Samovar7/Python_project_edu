'''
Напишите программу, которая получает целое число num и возвращает его
шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.

num = 16
test = num
base = 16
res =''
while num > 0:
    if num % base < 10:
        res = str(num % base) + res
        num = num // base
    else:
        match num % base:
            case 10:
                abcdef = 'A'
            case 11:
                abcdef = 'B'
            case 12:
                abcdef = 'C'
            case 13:
                abcdef = 'D'
            case 14:
                abcdef = 'E'
            case 15:
                abcdef = 'F'
        res = abcdef + res
        num = num // base
print(f'Шестнадцатеричное представление числа: {res}')
print(f'Проверка результата: {hex(test)}')
'''

'''
На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.

Напишите программу, которая должна возвращать сумму и произведение дробей.

Для проверки своего кода используйте модуль fractions.
'''

import fractions

def sum_frac (str1, str2):
    list_frac1 = str1.split(sep='/', maxsplit=2)
    list_frac2 = str2.split(sep='/', maxsplit=2)
    numerator = int(list_frac1[0]) * int(list_frac2[1]) + int(list_frac1[1]) * int(list_frac2[0])
    denominator = int(list_frac1[1]) * int(list_frac2[1])
    integer = 0
    if numerator == denominator:
        return print(f'Сумма дробей: 1/1')
    elif numerator < denominator:
        num = numerator
        dnum = denominator
    else:
        integer = numerator//denominator
        num = numerator - denominator * integer
        dnum = denominator
    i = 1
    while i < num // 2 + 1:
        if num % 2 == 0 and dnum % 2 == 0:
            num = num / 2
            dnum = dnum / 2
            i = 1
            continue
        if num % 3 == 0 and dnum % 3 == 0:
            num = num / 3
            dnum = dnum / 3
            i = 1
            continue
        if num % (6*i-1) == 0 and dnum % (6*i-1) == 0:
            num = num / (6*i-1)
            dnum = dnum / (6*i-1)
            i = 1
            continue
        if num % (6*i+1) == 0 and dnum % (6*i+1) == 0:
            num = num / (6*i+1)
            dnum = dnum / (6*i+1)
            i = 1
            continue
        i +=1
    if integer > 0:
        return print(f'Сумма дробей: {int(num)+int(dnum)*integer}/{int(dnum)}')
    return print(f'Сумма дробей: {int(num)}/{int(dnum)}')

def comp_frac (str1, str2):
    list_frac1 = str1.split(sep='/', maxsplit=2)
    list_frac2 = str2.split(sep='/', maxsplit=2)
    numerator = int(list_frac1[0]) * int(list_frac2[0])
    denominator = int(list_frac1[1]) * int(list_frac2[1])
    integer = 0
    if numerator == denominator:
        return print(f'Произведение дробей: 1/1')
    elif numerator < denominator:
        num = numerator
        dnum = denominator
    else:
        integer = numerator//denominator
        num = numerator - denominator * integer
        dnum = denominator
    i = 1
    while i < num // 2 + 1:
        if num % 2 == 0 and dnum % 2 == 0:
            num = num / 2
            dnum = dnum / 2
            i = 1
            continue
        if num % 3 == 0 and dnum % 3 == 0:
            num = num / 3
            dnum = dnum / 3
            i = 1
            continue
        if num % (6*i-1) == 0 and dnum % (6*i-1) == 0:
            num = num / (6*i-1)
            dnum = dnum / (6*i-1)
            i = 1
            continue
        if num % (6*i+1) == 0 and dnum % (6*i+1) == 0:
            num = num / (6*i+1)
            dnum = dnum / (6*i+1)
            i = 1
            continue
        i +=1
    if integer > 0:
        return print(f'Произведение дробей: {int(num)+int(dnum)*integer}/{int(dnum)}')
    return print(f'Произведение дробей: {int(num)}/{int(dnum)}')


frac1 = "7/35"
frac2 = "8/12"

sum_frac(frac1, frac2)
comp_frac(frac1, frac2)
a = fractions.Fraction(frac1)
b = fractions.Fraction(frac2)
print('Сумма дробей:', a+b)
print('Произведение дробей:', a*b)