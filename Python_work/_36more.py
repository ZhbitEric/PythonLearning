# -- coding: utf-8 --
# 一些补充知识

def get_details():
    return (2, 'detalis')


# a,b=<some expression> 会将表达式的结果解析成有两个值的元组
e, f = get_details()
print(e)
print(f)

# 这样就很容易实现两个数字的交换
a = 4
b = 8
a, b = b, a
print(a)
print(b)


