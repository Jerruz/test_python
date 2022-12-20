# import sys
# from pprint import pprint

# # pprint(sys.path)

# sys.path.append(r'C:\Users\mutovkin_av\Desktop\Груша брендбук')  # не отформатированный текст, чтобы не экранировать символ \

# pprint(sys.path)


ls_f = ['петя', 'маша','вася']

ns = 'Привет: {1:<15}, {0} '.format(*ls_f)

print(ns)