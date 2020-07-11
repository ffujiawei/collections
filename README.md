## 一段代码，解决一个小问题


### Go

- [有道云笔记去广告](go/youdao.go) 去除 Windows 有道云笔记主界面广告，必须以管理员权限运行，重启软件生效
- [网络事件监听与邮件提醒](go/remainder.go)
- [一个最简单的文件服务器](go/simpleweb.go)

### Python

- [PyPi 更换为国内镜像源](py/pypi.py)
- [Kali Linux 更换为国内镜像源](py/kali.py)
- [Ubuntu 更换为国内镜像源](py/ubuntu.py)


### 片段

* **铃声提醒** [2019-01-26]

```python
import winsound

# 仅可播放WAV格式的声音文件
winsound.PlaySound("sound.wav", winsound.SND_FILENAME)

# 异步，程序可在声音没有播完时继续执行后面的操作
winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
```

* **根用户运行**

```python
args = ' --no-sandbox --disable-infobars'

with open("/opt/google/chrome/google-chrome", 'a') as fp:
    fp.write(args)
```

* **截掉状态栏**

```python
from PIL import Image
from glob import glob

for img in glob('*.jpg'):
    n = Image.open(img)
    n = n.crop((0, 87, 1080, 2280))
    n.save(img)
```

* **拼接图像**

```python
from PIL import Image

def merge(c, q, n):
    c = Image.open(c)
    q = Image.open(q).resize((308, 308))
    new = Image.new('RGB', (621, 370), (255, 255, 255))
    new.paste(c, (31, 31))
    new.paste(q, (282, 31))
    new.save(n)
```
