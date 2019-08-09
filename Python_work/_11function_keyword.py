def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)


# 参数只认名称 不认顺序，和java不用
func(3, 7)
func(25, c=24)
func(c=50, a=100)
