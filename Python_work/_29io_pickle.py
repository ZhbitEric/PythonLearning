# -- coding: utf-8 --
# pickle是python提供的一个标准模块，用于将普通对象存在文件中，然后再将其恢复，这成为持久化存储对象
import pickle

shopListFile = 'shopList.data'

shopList = ['apple', 'banana', 'mango']

# w写 b(binary mode 二进制模式) t(text 文本模式)
f = open(shopListFile, 'wb')
pickle.dump(shopList, f)
f.close()

del shopList

f = open(shopListFile, 'rb')
shopList = pickle.load(f)
print(shopList)
f.close()
