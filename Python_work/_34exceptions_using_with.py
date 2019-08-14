# -- coding: utf-8 --
# with 语句 干净的完成try块获取资源，finally块中释放资源的模式

# with open 会自动关闭文件
# with使用一种协议 会获取open返回的对象 这里称为'thefile'
# 在启动下面的代码之前调用 thefile.__enter 在结束代码块的时候调用 thefile.__exit
# 所以我们最好不要像33中显示的使用try finally回收资源
with open('poem.txt')as f:
    for line in f:
        print(line, end=' ')
