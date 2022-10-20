ls = ['январь', 'февраль', 'март']
print(isinstance(ls, list))
a = 'B'
print(chr(ord(a)+32))

some_tuple = ('hello', True, 'word', 1, 2.2)
some_tuple_2 = 'hello', True, 'word', 1, 2.2

print(some_tuple)
print(some_tuple_2)

print(some_tuple == some_tuple_2)




a = [['hello'], 10]
b = a
print(id(a), id(b))
b[1] = 15
print(id(a), id(b))
print(a)
print(b)
print('===========================================================================')
from copy import deepcopy, copy
a = [['hello'], 10]
b = copy(a)
print(id(a), id(b))
print(a)
print(b)

b[1] = 11
b[0][0] = 33
print('===========================================================================')

print(a)
print(b)

print('--////////===========================================================================')


s = "28212" 
print(s.isdigit())
# contains alphabets and spaces s = "Mo3 nicaG el l22er"
print(s.isdigit())
