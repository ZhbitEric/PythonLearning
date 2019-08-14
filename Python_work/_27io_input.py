# -- coding: utf-8 --
# 输入输出


def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


# 去除语句中的标点和空格 Rise to vote, sir.
# 用元组
# todo:如何用这种方式去除语句中的符号空格
deleteItem = (' ', ',', '.')


def is_palindrome_2(text):
    return str(text).replace(' ', '').replace(',', '').replace('.', '').lower()


running = True

while running:
    something = input('Enter text:')
    something = is_palindrome_2(something)
    print(something)
    if is_palindrome(something):
        print('yes,is a palindrome')
    else:
        print('no, is not a palindrome')
        running = False
