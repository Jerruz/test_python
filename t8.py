
# ls = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
# 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

# for i in ls:
#     print('Привет,', (''.join(i.split()[-1:])).capitalize())



'''
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и
возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
содержащие имена, начинающиеся с соответствующей буквы. Например:
>>> thesaurus("Иван", "Мария", "Петр", "Илья")
{
"И": ["Иван", "Илья"],
"М": ["Мария"],
"П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется
сортировка по ключам? Можно ли использовать словарь в этом случае?

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Написать функцию thesaurus_adv(), принимающую в качестве аргументов
строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы
фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие
записи, в которых фамилия начинается с соответствующей буквы. 

Например:
>>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр
Алексеев", "Илья Иванов", "Анна Савельева")

{
"А": {"П": ["Петр Алексеев"]},

"И": {"И": ["Илья Иванов"]},

"С": {"И": ["Иван Сергеев", "Инна Серова"],"А": ["Анна Савельева"]}
}

Как поступить, если потребуется сортировка по ключам?

'''

# def tes(*args):
#     dic = {}
#     print(args)
#     for name in args:
#         dic.setdefault(name[:1], [])
#         dic[name[:1]].append(name)

#     print(dic)

# tes('Петя', 'Прокоп', 'Витя', 'Вася', 'Коля', 'Костя')

print('\n===========================================================\n')

