# -*- coding: utf-8 -*-
# @File : conf.py
# @Time : 2024-03-12 19:02
# @Author : chensiting
# @Email : 475707078@qq.com
# @Software: PyCharm
'''
if name 快捷键：输入main
'''

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
from selenium.webdriver.common.by import By
from common.times import dt_strftime
"""
配置文件总是项目中必不可少的部分！
将固定不变的信息集中在固定的文件中
这个conf文件我模仿了Django的settings.py文件的设置风格，但是又有些许差异
author: B站小北  time：2023-04-18
"""

class ConfigManager(object):
    """
    在这个文件中我们可以设置自己的各个目录，也可以查看自己当前的目录。

    遵循了约定：不变的常量名全部大写，函数名小写。看起来整体美观。
    """
    # 项目目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 页面元素目录
    ELEMENT_PATH = os.path.join(BASE_DIR, 'page_element')

    # 报告文件
    REPORT_FILE = os.path.join(BASE_DIR, 'report.html')

    # 邮件信息
    EMAIL_INFO = {
        'username': '475707078@qq.com',  # 切换成你自己的地址
        'password': 'QQ邮箱授权码',
        'smtp_host': 'smtp.qq.com',
        'smtp_port': 465
    }

    # 收件人
    ADDRESSEE = [
        '475707078@qq.com',
    ]

    # 测试网址
    BAIDU_URL = "https://www.baidu.com"
    ZHUIFENG = "https://exam.wzzz.fun"
    WPS_LOGIN = "https://account.wps.cn/"
    FILE_UPLOAD = "https://letcode.in/file"



cm = ConfigManager()
if __name__ == '__main__':
    print(cm.BASE_DIR)