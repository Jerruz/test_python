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

print({ddd.update({i:dic2[i]}) for i in list(dic2)})

print('63============================================')


a2 = sorted(dic2.items(), key=lambda x: x[1])  # сортировка словаря по значению. Можно написать пользовательскую функцию вместо lambda


print(dict(a2))

print('67=======================================================')


welcome = lambda user: print('Welcome, ' + user + '!')
welcome('Anon')

print('85=======================================================')





