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

str = ['привет сказочный мир', 'здравствуй моя планета']
new_str = []

for i in str:
    print(['-'.join(i.split())])
    new_str.extend(['-'.join(i.split())])

print(new_str)

# print('*****'.join(str))

# for i in str:
#     print(i)
#     print(type(i))


# str2 = 'привет сказочный мир'


# print('-'.join(str2.split()))
