# -*- coding: utf-8 -*-
# @File : test_login.py
# @Time : 2022-04-13 14:44
# @Author : chensiting
# @Email : 475707078@qq.com
# @Software: PyCharm
import allure,os

from common.baseAPI import ApiAssert
from utils.handle_path import report_path

print()
'''
测试用例执行条件：
1、业务层代码封装ok
2、需求自动化测试用例----数据驱动---使用指定文件类型
3、需要读取用例的用例名称、请求参数、预期结果、响应结果

结果：通过代码读取excel数据，取出后给test_login执行
'''
import pytest
from libs.login import Login
from utils.handle_excel import get_excel_data
'''
#核心：@pytest.mark.parametrize("变量"，所需要取的数据)
举例：@pytest.mark.parametrize("实际变量，预期变量"，['实际表达式的值计算',预期结果值])

'''
@allure.epic('外卖项目')
@allure.feature('登录模块')
class TestLogin:
    @pytest.mark.parametrize('title,inBody,expData',get_excel_data('登录模块','Login','标题','请求参数','响应预期结果'))
    @allure.title("{title}")
    def test_login(self,title,inBody,expData):
        res =Login().login(inBody)
        #断言:1-局部关键信息相等
        # assert res['msg'] == expData['msg']
        #2- 包含关系 in
        ApiAssert.define_api_assert(res['msg'],'=',expData['msg'])

if __name__ == '__main__':
    pytest.main(['test_login.py','-s','--alluredir',f'{report_path}','--clean-alluredir'])
    os.system(f'allure serve {report_path}')
