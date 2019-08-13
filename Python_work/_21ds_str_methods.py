name = 'Swaroop'

if name.startswith('swa'):
    print('swa')
elif name.startswith('Swa'):
    print('Swa')

if 'a' in name:
    print('a is in string')
# 返回位置 没有就是-1
print(name.find('a'))

if name.find('war') != -1:
    print('i\'m find')

# join 字符串拼接
delimiter = '_*_'
myList = ['dd', 'vv', 'aa']
print(delimiter.join(myList))

