# -- coding: utf-8 --
# 文件备份
import os
import time

# 1. The files and directories to be backed up are
# 双引号是为了保留字符串的空格
source = [r'C:\mydocuments']
# Example on Mac OS X and Linux:
# source = ['/Users/swa/notes']

# 2. The backup must be stored in a
target_dir = 'E:\\backup'
# Example on Mac OS X and Linux:
# target_dir = '/Users/swa/backup'

target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

print('zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('successful backup to', target)
else:
    print('backup Failed')
