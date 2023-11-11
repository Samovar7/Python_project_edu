'''
На вход подается словарь со списком вещей для похода в качестве ключа и их
массой max_weight в качестве значения.
Определите какие вещи влезут в рюкзак backpack передав его максимальную
грузоподъёмность.
Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и
сохранен в переменную backpack.
Достаточно получить один допустимый вариант и сохранить в переменную backpack.
Не выводите backpack на экран.
'''
'''
items = {
    "спальник": 1.5,
    "палатка": 3.2,
    "термос": 0.6,
    "карта": 0.1,
    "фонарик": 0.3,
    "котелок": 0.8,
    "еда": 2.5,
    "одежда": 1.7,
    "обувь": 1.2,
    "нож": 0.2
}
max_weight = 7.0
backpack = {}
max_weight_items = 0
for value in items.values():
    max_weight_items += value
#print(max_weight_items)
if max_weight_items > max_weight:
    diff = max_weight_items - max_weight
    backpack.update(items)
    for key, value in items.items():
        if diff - value <= 0:
            backpack.pop(key)
            break
        else:
            diff -= value
            backpack.pop(key)
else: backpack.update(items)
print(backpack)
'''

'''
В большой текстовой строке text подсчитать количество встречаемых слов и 
вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
Слова разделяются пробелами. Такие слова как don t, it s, didn t итд 
(после того, как убрали знак препинания апостроф) считать двумя словами.
Цифры за слова не считаем.
Отсортируйте по убыванию значения количества повторяющихся слов.
'''
'''
import string
import collections
text = "Python 3.9 is the latest version of Python. It's awesome!"
text = text.replace("'", " ")
clear_text = text.translate(str.maketrans('', '', string.punctuation))
clear_text = clear_text.lower()
clear_text = clear_text.split()
print(clear_text)

frequently_words = collections.Counter()
for word in clear_text:
    if word.isalpha():
        frequently_words[word]+=1
print(frequently_words.most_common(10))
'''

'''
На вход подается словарь со списком вещей для похода в качестве ключа и их 
массой max_weight в качестве значения.
Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
В переменную backpack сохраните словарь {предмет:вес} с вещами в рюкзаке.
В переменную result выведите список, содержащий все возможные варианты backpack. 
Напечатайте переменную result.
*Верните все возможные варианты комплектации рюкзака.
'''
'''
import itertools

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0
result = []
for i in range(1, len(items)+1):
    combination = itertools.combinations(items, i)
    for key in combination:
        s = 0
        backpack = {}
        for k in key:
            s += items[k]
        #print(round(s, 2))
        if round(s, 2) <= max_weight:
            for k in key:
                backpack[k] = items[k]
            result.append(backpack)
print('[', end='')
print(*[el for el in result], sep=',\n ', end=']')
'''

'''
Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами. 
В результирующем списке не должно быть дубликатов.
'''
lst = [1, 1, 2, 2, 3, 3, 5, 6, 7, 6]
duplicat = []
for el in lst:
    if lst.count(el) > 1:
        duplicat.append(el)
duplicat = list(set(duplicat))
print(duplicat)

