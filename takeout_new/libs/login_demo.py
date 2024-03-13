# -*- coding: utf-8 -*-
# @File : login_demo.py
# @Time : 2022-04-11 1:40
# @Author : chensiting
# @Email : 475707078@qq.com
# @Software: PyCharm
import requests

HOST = 'http://121.41.14.39:8082'
url = f'{HOST}/account/sLogin'
NAME_PSW = {'username':'dp0403','password':'b86ece4a7f0a30f0280d6b08980572dd'}

import hashlib
def get_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

get_md5('80051')

def login(inData,getToken=True):
    '''
    :param inData:账号+密码---字典
    :param getToken 为True 获取token; 为False 返回接口响应数据
    :return:
    '''
    inData['password'] = get_md5(inData['password'])
    payload = inData
    resp = requests.post(url,data=payload)
    # print(resp.text)

    if getToken == False:
        return resp.json()
    else:
        return resp.json()['data']['token']



if __name__ == '__main__':
    res=login({'username':'dp0403','password':'80051'})
    print(res)