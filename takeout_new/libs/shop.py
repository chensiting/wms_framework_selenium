# -*- coding: utf-8 -*-
# @File : shop.py
# @Time : 2022-04-18 12:13
# @Author : chensiting
# @Email : 475707078@qq.com
# @Software: PyCharm
import os
import pprint

from common.baseAPI import BaseAPI
from configs.config import NAME_PSW
from libs.login import Login
from utils.handle_path import testData_path


class Shop(BaseAPI):
    #1 列出店铺
    #2 更新店铺

    """
    店铺更新接口：数据从用例文件去读取  excel/yaml
        1- id  需要代码里去更新--字典可以更新值
        2- 图片信息需要传入
    """
    def update(self,inData,shopID,fileInfo):
        #1 - 更新传入id
        if inData['id'] == 'id不存在':
            inData['id'] = '0000'
        else:
            inData['id']=shopID
        #2 - 传入图片信息
        inData['image_path'] =fileInfo
        inData['image'] = f'/file/getImgStream?fileName={fileInfo}'
        print(inData)
        return super(Shop,self).update(inData)


if __name__ == '__main__':
    #1-登录--获取token
    token = Login().login(NAME_PSW,getToken=True)

    #2- 创建店铺实例
    shop = Shop(token)

    #3- 列出店铺
    testData ={'page':1,'limit':20}
    res = shop.query(testData)
    # pprint.pprint(res)

    #---------获取店铺id--------------
    shopID = res['data']['records'][0]['id']

    #4- 文件上传
    res2 = shop.file_upload(os.path.join(testData_path,'timg.jpg'))
    # print(res2)
    fileInfo = res2['data']['realFileName']

    #5-更新店铺，传数据
    shopData = {
        "name": "cst",
        "address": "深圳市福田区333号",
        "id": "3269",
        "Phone": "13176876632",
        "rating": "6.0",
        "recent_order_num":100,
        "category": "快餐便当/简餐",
        "description": "满30减5，满60减8",
        "image_path": "b8be9abc-a85f-4b5b-ab13-52f48538f96c.png",
        "image": "http://121.41.14.39:8082/file/getImgStream?fileName=b8be9abc-a85f-4b5b-ab13-52f48538f96c.png"
    }
    res3 = shop.update(shopData,shopID,fileInfo)
    # print(res3)