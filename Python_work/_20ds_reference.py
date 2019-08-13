# 引用
shopList = ['apple', 'mango', 'carrot', 'banana']
myList = shopList

del shopList[0]
print(shopList)
print(myList)

# 这样的引用就没有指向同一个对象了
myList = shopList[:]  # 切片操作，相当于循环复制拿元素出来
print(myList)
del myList[0]
print(shopList)
print(myList)
