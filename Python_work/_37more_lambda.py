# -- coding: utf-8 --
# lambda表达式
points = [{'x': 2, 'y': 8}, {'x': 4, 'y': 1}]
points.sort(key=lambda i: i['y'])
print(points)

