# 序列（列表、元组、字符串 lists, tuples and strings）的特性
# 下面只是举例list和string 其他也适用

shopList = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

print(shopList[1])
print(shopList[-1])
print(name[0])
print(name[-1])
# 切片操作
print(shopList[:])
print(name[:])
print(shopList[2:])
print(name[3:])
# 表示下标1到2的元素
print(shopList[1:3])
print(name[1:-1])
# 步长
print(shopList[::1])
# 神奇 这样序列就倒过来了
print(shopList[::-1])
print(name[::3])
print(name[::-1])

print(shopList.__class__)
print(name.__class__)

# set集合
setbir = set(['aaa', 'bbb', 'ccc'])
print('aaa' in setbir)
print(1 in setbir)
setbirrrrr = setbir.copy()
setbirrrrr.add('ddd')
print(setbirrrrr.issuperset(setbir))
print(setbirrrrr.issubset(setbir))
print(setbir & setbirrrrr)
print(setbir | setbirrrrr)
print(setbir ^ setbirrrrr)

setbir.remove('aaa')
print(setbir)

