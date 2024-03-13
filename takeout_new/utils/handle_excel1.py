# -*- coding: utf-8 -*-
# @File : handle_excel1.py
# @Time : 2022-04-13 14:49
# @Author : chensiting
# @Email : 475707078@qq.com
# @Software: PyCharm
import os.path

from utils.handle_path import testData_path

print()
'''
V1.0需求：
---------------版本 v1.0---------------
需求：有可能客户或者上下游同事，描述不是很专业
    1- 获取自动化测试用例 excel里面的对应的数据---大功能   
分析需求：
    1- 获取具体哪些数据
        1- 用例标题
        2- 请求body
        3- 预期响应结果
    2- 需要返回什么类型
        1- 客户需要把读取的数据给test_login()   使用的是pytest--数据驱动的方法
            [(),(),()]
解决方案：
    1- 操作execcl库是什么
        1- xlrd  xlwt  操作xx.xls----选定
            xlrd 读操作
            xlwt 写操作---新建一个文件
            xlutils 写操作  在已有的excel文件里修修改（写）
        2- openpyxl   操作xx.xlxs
        3- panda  大数据场景
测试反馈：
版本迭代建议：
"""
'''
import xlrd
def get_excel_data(exceldir,sheetName):
    #1、打开文件
    workBook = xlrd.open_workbook(exceldir,formatting_info=True)

    #2、获取所有表名
    sheets1 = workBook.sheet_names()
    # print(sheets1)
    #3、获取某一表名
    workSheet = workBook.sheet_by_name(sheetName)
    # print(workSheet)
    #4、获取一列数据
    col = workSheet.col_values(0)
    # print(col)
    #5、获取一行数据
    row = workSheet.row_values(0)
    # print(row)
    #6、获取单元格数据-workSheet.cell(行编号,列编号)
    cell = workSheet.cell(0,0).value
    # print(cell)

#------------------获取对应需求的数据--------------------------
    #目的：需要获取 请求参数，响应预期结果
    resList = []
    rowIndex = 0
    for one in workSheet.col_values(0):
        reqBody = workSheet.cell(rowIndex,9).value
        respData = workSheet.cell(rowIndex,11).value
        resList.append((reqBody,respData))
        rowIndex +=1
    # print(resList)

    for one in resList:
        print(one)

if __name__ == '__main__':
    filedir = os.path.join(testData_path,'Delivery_System_V1.5.xls')
    # print(filedir)
    get_excel_data(filedir,'登录模块') #['登录模块', '我的商铺', '食品管理', '我的订单', '修改密码']

