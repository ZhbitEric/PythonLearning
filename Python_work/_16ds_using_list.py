#列表
shopList = ['apple', 'mango', 'carrot', 'banana']
print(len(shopList))

for item in shopList:
    print(item + ',', end='')
print('===========')
shopList.append('aaaa')
print(shopList)

shopList.sort()
print(shopList)

print(shopList[0])

oldItem = shopList[0]
del shopList[0]
print(oldItem)
print(shopList)
