# 位于参数列表末尾的才能被赋默认值，不能 只赋值第一个 不赋值后面的
def say(message='5', time=1):
    print(message * time)


say('hello')
say('he\'', 4)
say('')
