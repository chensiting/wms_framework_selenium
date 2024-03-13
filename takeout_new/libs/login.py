# -*- coding: utf-8 -*-
# @File : login.py
# @Time : 2022-04-12 2:23
# @Author : chensiting
# @Email : 475707078@qq.com
# @Software: PyCharm
import copy

from common.baseAPI import BaseAPI
from configs.config import NAME_PSW
from utils.handle_data import get_md5

class Login(BaseAPI):
    def login(self,inData,getToken=False):
        inData = copy.copy(inData)  #浅拷贝下数据--避免修改全局数据
        inData['password']=get_md5(inData['password'])
        respData = self.request_send(data=inData)
        # print(respData)
        if getToken:    #获取token值
            return respData['data']['token']
        else:       #获取登录返回值
            return respData



if __name__ == '__main__':
    print(Login().login(NAME_PSW)) #  {'login': {'path': '/account/sLogin', 'method': 'POST'}}
