# -*- coding: utf-8 -*-
# @File : handle_data.py
# @Time : 2022-04-13 14:21
# @Author : chensiting
# @Email : 475707078@qq.com
# @Software: PyCharm


import hashlib
def get_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


if __name__ == '__main__':
    print(get_md5('80051'))
