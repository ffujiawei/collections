'''
    铃声提醒示例
'''

import winsound
from time import sleep

from cerium import AndroidDriver
from requests_html import HTMLSession


driver = AndroidDriver(wireless=True, host='192.168.124.12')


def withdraw():
    driver.unlock((29281 - 0.5) / 3.14)  # unlock by password
    sleep(3)
    # menu
    driver.long_press(570, 1560, 1000)
    sleep(3)
    # withdraw
    driver.long_press(620, 980, 1000)
    sleep(3)
    driver.lock()


headers = {
    'Host': 'm.58139.com',
    'Proxy-Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'DNT': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://m.58139.com/m/user/index/code/sHcIypNz20',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cookie': 'PHPSESSID=c969a3jucs2ockuge4v5dp5e97; ggz_code=sHcIypNz20',
}

requests = HTMLSession()

num = 13
while True:
    print('Working....')
    try:
        r = requests.get('http://m.58139.com/m/user/send', headers=headers)
    except:
        print('Die...')
        continue
    lst = r.html.xpath('//td[@class="inyc cent"]/text()')
    n = lst.count('快乐的????娜粉们')
    print(num, n)
    if n != num:
        winsound.PlaySound("sound.wav", winsound.SND_FILENAME)
        print(num, n)
        withdraw()
        num = n
        sleep(60)
    sleep(60)
