# -*- coding: utf-8 -*-
# @File : handle_path.py
# @Time : 2022-04-13 14:56
# @Author : chensiting
# @Email : 475707078@qq.com
# @Software: PyCharm

import os

# print(__file__)
# print(os.path.dirname(__file__))
# print(os.path.dirname(os.path.dirname(__file__)))
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#1- 工程路径
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(project_path)

#2- 配置路径
config_path = os.path.join(project_path,'configs')
#print(config_path)

#3- 测试数据路径
testData_path = os.path.join(project_path,'data')
#print(testData_path)

#4- 测试报告路径
report_path = os.path.join(project_path,r'outFiles\report\tmp')
#print(report_path)

#5- log路径
log_path = os.path.join(project_path,r'outFiles\logs')
#print(log_path)

#6- yaml路径
