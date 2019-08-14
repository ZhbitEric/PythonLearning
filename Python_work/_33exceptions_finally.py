# -- coding: utf-8 --
import sys
import time

f = None

try:
    f = open('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()
        print('press ctrl+c now')
        time.sleep(2)
except IOError:
    print('Could not find file poem.txt')
except KeyboardInterrupt:
    print('!! You cancelled the reading from the file.')
finally:
    # 赋值为0或NONE的变量或者空序列或集合的变量，都被Python视为FALSE
    if f:
        f.close()
    print('closed the file')
