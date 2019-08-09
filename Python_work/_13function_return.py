def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'equal'
    else:
        return y


print(maximum(2, 3))


# 每个函数都隐式包含一个返回none的语句
def some_function():
    pass  # 表示空代码块


print(some_function())
