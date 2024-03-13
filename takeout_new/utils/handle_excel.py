# -*- coding: utf-8 -*-
# @File : handle_excel1.py
# @Time : 2022-04-13 14:49
# @Author : chensiting
# @Email : 475707078@qq.com
# @Software: PyCharm
import os.path

from utils.handle_path import testData_path
"""
---------------版本 v3.0---------------
需求：    
    1- 需要对测试用例进行挑选 
        全部：1，2，3，4，5
        挑选出：优先级高/特定用例bug回归
分析需求：
    用例挑选的方式：
        1- 全部 all
        2- 只选择某一个用例  tc001
        3- 连续的用例  tc003-tc005
        4- 复合型  ['tc003','tc007-tc009','tc010']
解决方案：

测试反馈：
    函数调用的参数传递的太多！
        get_excel_data(fileDir,'登录模块','Login','URL','标题','前置条件')
版本迭代建议：

"""



import xlrd
def get_excel_data(sheetName,caseName,*args,runCase=['all'],exceldir=None):
# def get_excel_data(exceldir,sheetName,caseName,*args,runCase=['all']):
    exceldir = os.path.join(testData_path,'Delivery_System_V1.5.xls')
    """
    :param excelDir: 用例文件路径
    :param sheetName: 选择的sheet表
    :param caseName: 用例名
    :param args: 获取的数据
    :param runCase: 筛选的用例
    :return: [(),()]
    """
    resList = []    #存放结果 [(请求1，响应1),(请求2，响应2)]
    workBook = xlrd.open_workbook(exceldir,formatting_info=True)
    workSheet = workBook.sheet_by_name(sheetName)   #3、获取需要操作的子表

#------------------V2.0.2用户传入需要获取的列，代码去获取对应列的单元格数据--------------------
    colIndexList = []   #存放用户输入列名对应的列编号
    for i in args:
        colIndexList.append(workSheet.row_values(0).index(i))
    # print(colIndexList) #[2, 5, 4]

#------------------V3.0用例筛选-----------------------------------------------------
    #runCase = ['all','003','007-009','010']
    runList = []
    if 'all' in runCase:
        runList = workSheet.col_values(0)   #全部选择
    else:
        for one in runCase :
            if '-' in one:  #连续 -------> ['name001','name002']
                start,end = one.split('-')
                for i in range(int(start),int(end)+1):
                    runList.append(caseName+f'{i:0>3}')
            else:   #不连续
                runList.append(caseName+f'{one:0>3}')
    # print(runList)

#------------------V1.0获取对应需求的数据--------------------------------------------------
    rowIndex = 0
    for one in workSheet.col_values(0):
#------------------V2.0.1--根据子表-----自动筛选测试用例名----------------------------------
        if caseName in one and one in runList:
            getcolData = []
            for num in colIndexList:
                tmp = workSheet.cell(rowIndex,num).value
                if is_json(tmp):
                    tmp = json.loads(tmp)
                getcolData.append(tmp)
            resList.append(list(getcolData))
        rowIndex +=1

    return resList
    # for one in resList:
    #     print(one)

import json
def is_json(inData:str):
    try:
        json.loads(inData)
        return True
    except:
        return False



if __name__ == '__main__':
    # filedir = os.path.join(testData_path,'Delivery_System_V1.5.xls')
    get_excel_data('登录模块','Login','标题','请求参数','响应预期结果') #['登录模块', '我的商铺', '食品管理', '我的订单', '修改密码']

