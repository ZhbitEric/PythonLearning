def print_max(x, y):
    '''文本注释.

    :param x:
    :param y:
    :return:'''
    # convert to integers, if possible
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is max')
    elif x < y:
        print(y, 'is max')


print_max(3, 5)
print(print_max.__doc__)
help(print_max)
