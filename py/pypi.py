'''
    PyPi 更换为国内镜像源
'''

import sys
import os

mirrors = '''\
[global]
index-url=http://mirrors.aliyun.com/pypi/simple/

[install]
trusted-host=mirrors.aliyun.com
'''

# index-url = https://mirrors.ustc.edu.cn/pypi/web/simple/
# extra-index-url = https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/\

user = os.path.expanduser('~')
if sys.platform == 'win32':
    os.mkdir(f"{user}/AppData/Roaming/pip")
    with open(f"{user}/AppData/Roaming/pip/pip.ini", 'w', encoding='utf-8') as fp:
        fp.write(mirrors)
elif sys.platform == 'linux' or sys.platform == 'darwin':
    os.mkdir(f"{user}/.pip")
    with open(f"{user}/.pip/pip.conf", 'w', encoding='utf-8') as fp:
        fp.write(mirrors)
