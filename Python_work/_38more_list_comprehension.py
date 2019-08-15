# -- coding: utf-8 --
# list推导
# 非常方便的使用老list生成新的list
listOne = [2, 3, 4]
listTwo = [2 * i for i in listOne if i > 2]
print(listOne)
print(listTwo)


# 可变参数数量
def powersum(power, *args):
    total = 0
    for i in args:
        total += pow(i, power)
    return total


print(powersum(2, 3, 4))
