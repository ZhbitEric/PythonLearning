import sys

print('the command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')

import os

print(os.getcwd())

# dir是内置的，返回由对象定义的名称列表，如果是模块，则此列表包括模块内定义的函数、类和变量
print(dir())

print(dir(sys))

a = 5
print(dir())

del a
print(dir())

help(list)
