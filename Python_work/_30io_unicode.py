# -- coding: utf-8 --
# 字符串编码
import io

# encoding只在文本模式（t）下才使用
f = io.open('abc.txt', 'wt', encoding='utf-8')
f.write(u'Imagine non-English language here')
f.close()

text = io.open('abc.txt', encoding='utf-8').read()
print(text)
