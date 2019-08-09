age = 20
name = 'Swaroop'
print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

print(name + ' is ' + str(age) + ' years old ')

print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))
print('==============')
print('{name} was {age} years old when he wrote this book'.format(name=name, age=age))
print('Why is {name} playing with that python?'.format(name=name))
print('==============')
print(f'{name} was {age} years old when he wrote this book')  # notice the 'f' before the string
print(f'Why is {name} playing with that python?')  # notice the 'f' before the string
print('==============')
# decimal (.) precision of 3 for float '0.333'
print('{:.4f}'.format(1.0 / 3))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^111}'.format('hello'))
# keyword-based 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
print('==============')
print('a', end='')
print('b', end='')
print('==============')
print('a', end=' ')
print('b', end=' ')
print('c')
print('==============')
# 反斜杠的作用是显示的将多个物理行连接
print("Newlines are \
indicated by \n")
print(r"Newlines are indicated by \n")
