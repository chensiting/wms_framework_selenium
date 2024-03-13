# -*- coding: utf-8 -*-
# @File : conftest.py
# @Time : 2024-03-12 17:08
# @Author : chensiting
# @Email : 475707078@qq.com
# @Software: PyCharm
#Description : 产生driver

import pytest
from selenium import webdriver


"""
conftest.py测试框架pytest的胶水文件，里面用到了fixture的方法，封装并传递出了driver。
test_pytest.fixture 这个实现了和unittest的setup，teardown一样的前置启动，后置清理的装饰器。

管理数据库连接，全局管理我们的driver
"""

@pytest.fixture(scope='session', autouse=True)
def drivers():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
