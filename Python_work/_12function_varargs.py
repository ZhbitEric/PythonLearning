# 可变形参 *会把参数收集成一个元组 **会把参数收集成一个字典
def total(a=5, *numbers, **phonebook):
    print('a', a)

    for single_item in numbers:
        print('single_item', single_item)

    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


total(10, 2, 3, 4, 5, 6, c=2, r=3, Damon='damon')
