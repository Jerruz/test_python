# import sys
# from pprint import pprint

# # pprint(sys.path)

# sys.path.append(r'C:\Users\mutovkin_av\Desktop\Груша брендбук')  # не отформатированный текст, чтобы не экранировать символ \

# pprint(sys.path)




# dic = {'name': 'bob', 'age': 23, 'sex':'male'}

# print('{0[name]} {0[sex]} {0[age]}'.format(dic))  # подстановка из словаря

lst = [1,3,5,7,8,9]

lst[1:3] = lst[-3:-1]  # можно заменить один срез другим
print(lst)

# print(lst[-3:-1])


