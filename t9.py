dic = {'a':[1,2,3], 'b':[11,22,33]}

# for i in ['a','b']:
#     dic[i].append(444)


# for i in ['c']:
#     dic[i].extend([555, 777, 888])

dic.setdefault('c', {})

dic['c'].update({'f':['pit','pol']})

print(dic)

