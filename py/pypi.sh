mkdir ~/.pip
echo "[global]
index-url=http://mirrors.aliyun.com/pypi/simple/

[install]
trusted-host=mirrors.aliyun.com
" >~/.pip/pip.conf


echo "[global]
index-url = https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/

[install]
trusted-host=mirrors.tuna.tsinghua.edu.cn
" >~/.pip/pip.conf