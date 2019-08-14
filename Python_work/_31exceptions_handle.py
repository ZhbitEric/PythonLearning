# -- coding: utf-8 --
# 捕获异常

try:
    text = input('Enter something -->')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('You entered {}'.format(text))

# except 后面没见错误参数就是全部
try:
    text = input('--->')
except:
    print('all exceptions')

try:
    text = input('a--->')
except (EOFError, KeyboardInterrupt):
    print('some exceptions')
