# s_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
#           'была', '+5', 'градусов']

# new_list = []
# for i in s_list:
#     if i.isdigit():
#         new_list.extend(['"', f'{int(i):02}', '"'])
#     elif (i.startswith('+') or i.startswith('-')) and i[1:].isdigit():
#         new_list.extend(['"', f'{i[0]}{int(i[1:]):02}', '"'])
#     else:
#         new_list.append(i)

# tot = ' '.join(new_list)
# print(tot)

from turtle import pensize


# str = ['привет сказочный мир', 'здравствуй моя планета']
# new_str = []

# for i in str:
#     print(['-'.join(i.split())])
#     new_str.extend(['-'.join(i.split())])

# print(new_str)

# print('*****'.join(str))

# for i in str:
#     print(i)
#     print(type(i))


# str2 = 'привет сказочный мир'


# print('-'.join(str2.split()))

print('=======================================================')


dic1 = {
    'name': 'pol',
    'sername': 'lansky',
    'age': '55',
    'position': 'manager'
}

a1 = sorted(dic1.items())  # сортировка словаря по ключу


print(dict(a1))

dic2 = {
    'name': 'pol',
    'sername': 'lansky',
    'age': '55',
    'position': 'manager'
}
print('61============================================')
ddd = {}
# d = list(dic2)
for i in list(dic2):
    d33 = {i:dic2[i]}
    ddd.update(d33)
print(ddd)


print('63============================================')


a2 = sorted(dic2.items(), key=lambda x: x[1])  # сортировка словаря по значению. Можно написать пользовательскую функцию вместо lambda


print(dict(a2))

print('67=======================================================')


welcome = lambda user: print('Welcome, ' + user + '!')
welcome('Anon')

print('85=======================================================')

dic3 = {
    'name': 'pol',
    'sername': 'lansky',
    'age': '55',
    'position': 'manager'
}

dic4 = { 'Alexandra' : 27,
            'Shelina Gomez' : 22, 
            'James' : 29, 
            'Peterson' : 30 
}

dic33 = dic3.copy()

for key, item in dic4.items():
    dic33[key] = item


print(dic33)
print(dic3)
print(dic4)

dic4.update(shmeterson = 55, buetrson = 77)

print(dic4)

dic5 = {**dic1, **dic4}
print('115==========================================')
print(dic5)


vv = {'dd': 5, 'ff':'l'}
print(vv)


ls = ['петя', 'коля', 'вася', 'сережа']

d = dict.fromkeys(ls, 1)

print(d)
d1 = {}

for key, val in d.items():
    val += 1
    d[key] = val


print(d)

print(d.get('юля', d.setdefault('юля', 5)))  # Если имя Юля не встречается, то добавляем ее в словарь со значением 5

print(d)
print('===============================')

f = d.setdefault('даша', 7)

print(f)

print(d)

print('===============================')


sk = d.keys()

sk=list(sk)

sk.sort()

print(sk)