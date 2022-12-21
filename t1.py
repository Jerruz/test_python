from cgi import print_arguments
import collections

from pickletools import stringnl_noescape_pair
from typing import Counter
import sys
from os import path
from weakref import proxy


# a = 'абракадабра'
# print(a)

# b = list(range(5))

# lt = collections.Counter(a)
# print(lt)

# print('=================================')


# d = lt['а']  # обращение к элементу словаря по ключу

# print(d)

# print('23=================================')

# print(lt)
# print(list(lt.elements()))  # преобразует словарь в список

# v1 = 'привет'
# print(v1[2::-1])

# print('1=================================')

# s = collections.Counter('ffkslskrirqsisdhfk')
# d = Counter('asdfafebaf')
# print(d)
# print('2=================================')


# print(s)

# print(list(s.elements()))

# print('=================================')

# dic = Counter({'name': 3, 'sername': 2})

# print(list(dic.elements()))


# print(v1.capitalize())

# ag = frozenset('sd', 'fg', 'hj')

# print('=================================')

# a = 'привет, мир!'
# print(a.index(' '))


# print('=================================')

# name2 = 'ваня'
# age2 = 33.23

# # print(type(age))

# print('Уважаемый %(name)s, вам сегодня %(age)15.2f года' %{'name' : 'петя', 'age' : 3.75})

# print('Уважаемый %s с возрастом %015.5f' %(name2, age2))

# print('=================================')

# print('привет {0:<10}, из {1} с индексом {2:>015.08f} и номером {3:07d}'.format('POL', 'MOSCOW', 15.11, 5))

# print('=================================')

# ls_f = ['петя', 'маша','вася']

# ns = 'Привет: {1:<15}, {0} '.format(*ls_f)

# print(ns)

# print('=================================')

# ls_f = ['петя', 'маша','вася']

# ns = 'Привет: {0[0]}, {1[1]} ===== {2}'.format(ls_f, ls_f, ls_f[-1])  # отрицательный срез можно указать только через format

# print(ns)

# print('=================================')

# import sys

# nws = 'добрый день, {sys_m.platform} === {name[n1]}'.format(sys_m=sys, name = {'n1':'юля', 'n2':'маша', 'n3': 'сережа'})

# print(nws)


# print('=================================')

# res = '{0:.{1}f}'.format(1/3.0, 7)  # ????????????????????

# print(res)


# print(format(1.23256, '010.2f'))
# print(format(1345325.334436, '015,.2f'))  # можно уазать разделитель групп разрядов в виде запятой

# print('=================================')

# url = 'https://geekbrains.ru/teacher/lessons/79615'

# print(url.split('/'))
# prot, *all = url.split('/')
# print(prot[:-1], '----', all )


# print('=================================')



# print('=================================')

# a, *s = 2,3,4,5,6,7
# print(a,tuple(s))

# qq,ww,ee = 11,22,33
# print(qq)
# print('довдыожд=================================')

# print('довдыожд=======23423423424==========================')


# s = "5"
# print(s.isdigit())


# l1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# l2 = []

# for i in l1:
#     if i.isdigit() or i.startswith('+') or i.startswith('-'):
#         i = int(i)
#         i = f'{i:02d}'
#         l2.append(i)

#     else:
#         l2.append(i)

# print(l2)

print('=================================')


# ls = ['pol', 'pit', 'den']

# def mn(data: list) -> str:
#     for i in range(3):
#         print(f'меня зовут {data[i]}')


# mn(ls)



