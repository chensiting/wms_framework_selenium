# -*- coding: utf-8 -*-
# @File : baseAPI.py
# @Time : 2022-04-11 11:35
# @Author : chensiting
# @Email : 475707078@qq.com
# @Software: PyCharm
import inspect

import requests
from utils.handle_yml import get_yaml_data
from configs.config import HOST

class BaseAPI:
    def __init__(self,inToken=None): #希望任何类在继承这个方法，可以在初始化时把对应配置文件读取出来
        self.data = get_yaml_data('../configs/apiConfig.yml')[self.__class__.__name__]
        if inToken:
            self.header = {'Authorization':inToken}
        else:
            self.header=None

    def request_send(self,data=None,json=None,param=None,file=None): #发送方法
        methodName = inspect.stack()[1][3]
        path,method = self.data[methodName].values()
        # print(type(self.data[methodName]))
        # print('谁调用我',methodName)

        resp = requests.request(url=HOST+path,method=method,data=data,json=json,params=param,headers=self.header,files=file)

        # print(methodName,'---',self.data[methodName])
        return resp.json()

    def add(self,inData):
        return self.request_send(param=inData)

    def delete(self):
        pass

    def update(self,inData):
        return self.request_send(param=inData)

    def query(self,inData):
        return self.request_send(param=inData)

#优化传入参数 d:/123.png
    # def file_upload(self,fileName,fileDir,fileType):
    def file_upload(self,fileDir:str):
        fileName = fileDir.split('/')[-1]
        fileType = fileDir.split('.')[-1]
        userFile = {'file':(fileName,open(fileDir,mode='rb'),fileType)}
        return self.request_send(file=userFile)

class ApiAssert:
    @classmethod  #类方法
    def define_api_assert(cls,result,condition,exp_result):
        """
        :param result:实际结果
        :param condition: 条件
        :param exp_result:预期结果
        :return:
        """
        try:
            if condition == '=':
                assert result == exp_result

            elif condition == 'in':
                assert exp_result in result
        except Exception as error:
            #日志
            pass
            raise error