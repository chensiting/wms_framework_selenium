# -*- coding: utf-8 -*-
#!/usr/bin/env python
# @File : test_001_login.py
# @Time : 2024-03-12 17:55
# @Author : chensiting
# @Email : 475707078@qq.com
# @Software: PyCharm


import pytest
from pages.index_page.index import zhuifeng_index_page
from conf.conf import ConfigManager
import time
from common.image_identify import image_identify


"""
test_pytest.fixture + 生成器yield   一起实现了和unittest的setup，teardown一样的前置启动，后置清理的装饰器
"""


class TestSearch:
    @pytest.fixture(scope='function', autouse=True)
    def open_index(self, drivers):
        """打开百度"""
        drivers.get(ConfigManager.BAIDU_URL)
        yield
        print("后置")

    @pytest.mark.smoke
    @pytest.mark.parametrize('username, password', [
        ('wzz', '12345')
    ])
    def test_001(self, drivers, username, password):
        zhufeng = zhuifeng_index_page(drivers)    #类的实例对象，这个对象=zhufeng
        zhufeng.input_account = username    #zhufeng（代替上面的类）.每一个元素
        zhufeng.input_password = password
        # zhufeng.log_in_button.click()
        zhufeng.image_code = image_identify(drivers, zhufeng.image,  '简单验证码.png', 'crop_pic.png')
        zhufeng.click_log_in_button #登录按钮
        time.sleep(3)




if __name__ == '__main__':
    pytest.main(['vs', 'testcases/test_pytest/test_search_baidu_index.py'])
