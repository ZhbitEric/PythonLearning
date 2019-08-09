def print_max(a, b):
    if a > b:
        print(a, ' is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, ' is maximum')


while True:
    x = int(input('x='))
    y = int(input('y='))
    print_max(x, y)
