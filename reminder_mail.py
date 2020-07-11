'''
    邮件提醒示例
'''

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from time import sleep

import requests
from platinum import generate_user_agent

xjqy = "http://xjqy.telefen.com/starlevel/yaduo/Commodity/Detail?commodityId=222432"
user_agent = generate_user_agent(device_type="smartphone")

smtp = 'smtp.139.com'
sender = '18268237856@139.com'
addrs = ['1748202178@qq.com']


message = MIMEText('谢谢你的关注！', 'plain', 'utf-8')
message['From'] = Header('18268237856@139.com', 'utf-8')
Subject = '你好呀，芒果TV会员上架了，快抢！'
message['Subject'] = Header(Subject, 'utf-8')

while True:
    response = requests.get(xjqy, headers={'User_Agent': user_agent})
    if response.url == xjqy:
        smtp = smtplib.SMTP(smtp)
        smtp.login('18268237856@139.com', 'fjw12345678')
        for addr in addrs:
            smtp.sendmail(sender, addr, message.as_string())
        smtp.quit()
        break
    sleep(600)