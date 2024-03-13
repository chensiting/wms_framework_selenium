# -*- coding: utf-8 -*-
# @File : handle_excel1.py
# @Time : 2022-04-13 14:49
# @Author : chensiting
# @Email : 475707078@qq.com
# @Software: PyCharm
import os.path

from utils.handle_path import testData_path


"""
---------------版本 v2.0---------------
需求：    
    1- 需要传递一个对应的接口的筛选的条件 
    2- 提供扩展性  以后可能需要获取用例标题
分析需求：
解决方案：
    1- 我们不清楚后续需要获取哪些列数据--可以考虑使用可变数量参数  *args
测试反馈：
版本迭代建议：

"""
import xlrd
def get_excel_data(exceldir,sheetName,caseName,*args):
    '''
    :param exceldir: 用例文件
    :param sheetName: 表名
    :param caseName: 用例名   要去哪个数据做个判断------自动筛选----建议用用例编号区分
    :return:
    '''
    resList = [] #存放结果 [(请求1，响应1),(请求2，响应2)]
    #1、打开文件
    workBook = xlrd.open_workbook(exceldir,formatting_info=True)

    workSheet = workBook.sheet_by_name(sheetName)   #3、获取需要操作的子表

    # print(workBook.sheet_names()) #2、获取所有的子表
    # print(workSheet.col_values(0))    # #4、获取一列数据
    # print(workSheet.row_values(0))    # #5、获取一行数据
    # print(workSheet.cell(0,0).value)  # #6、获取单元格数据-workSheet.cell(行编号,列编号)

#方案：用户传递  args---元组类型  ('URL'，'标题','请求体')
#------------------V2.0.2用户传入需要获取的列，代码去获取对应列的单元格数据--------------------
    colIndexList = []   #存放用户输入列名对应的列编号
    for i in args:
        # print(workSheet.row_values(0).index(i))
        colIndexList.append(workSheet.row_values(0).index(i))
    print(colIndexList) #[2, 5, 4]

#------------------V1.0获取对应需求的数据--------------------------
    #目的：需要获取 请求参数，响应预期结果
    rowIndex = 0
    for one in workSheet.col_values(0):
#------------------V2.0.1--根据子表-----自动筛选测试用例名------------------------
        if caseName in one:
            getcolData = []
            for num in colIndexList:
                # reqBody = workSheet.cell(rowIndex,9).value  #请求参数
                # respData = workSheet.cell(rowIndex,11).value    #响应预期结果
                # resList.append((reqBody,respData))  #[(请求1，响应1),(请求2，响应2)]
                tmp = workSheet.cell(rowIndex,num).value
                getcolData.append(tmp)
            resList.append(list(getcolData))
        rowIndex +=1
    # print(getcolData)       #['登录认证', '/account/sLogin', '用户名错误，密码正确']
    # print(resList)

    for one in resList:
        print(one)

if __name__ == '__main__':
    filedir = os.path.join(testData_path,'Delivery_System_V1.5.xls')
    # print(filedir)
    get_excel_data(filedir,'登录模块','Login','接口名称','URL','标题') #['登录模块', '我的商铺', '食品管理', '我的订单', '修改密码']

