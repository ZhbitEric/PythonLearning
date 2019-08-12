# 元组，与列表类似，但是特点是和字符串一样，即不能修改元组

zoo = ('python', 'elephant', 'penguin')
print('zoo:', len(zoo))

newZoo = 'monkey', 'camel', zoo
print('newZoo:', len(newZoo))

print('zoo::', zoo)
print('newZoo::', newZoo)
print("newZoo[2]::", newZoo[2])
print("newZoo[2][2]::", newZoo[2][2])

# 一个元素的元组要用逗号来识别
singleton = (2,)
print(len(singleton))
print(singleton.__class__)

# 这样没有逗号就变成字符串了
singleton_2 = ('aaa')
print(singleton_2.__class__)
