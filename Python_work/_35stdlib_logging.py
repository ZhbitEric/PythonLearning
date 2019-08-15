# -- coding: utf-8 --
# 标准库
import logging  # 日志模板模块
import os  # 与系统交互的模块
import platform  # 平台模块 获取平台的相关信息，即操作系统
import sys

print(sys.version_info)

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')

print('Logging to ', logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w'
)

logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")
