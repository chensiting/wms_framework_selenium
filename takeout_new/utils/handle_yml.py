# -*- coding: utf-8 -*-
# @File : handle_yml.py
# @Time : 2022-04-12 2:10
# @Author : chensiting
# @Email : 475707078@qq.com
# @Software: PyCharm
import yaml


def get_yaml_data(filedir):
    with open(filedir,encoding='utf-8') as fo:
        return yaml.safe_load(fo.read())




if __name__ == '__main__':
    print(get_yaml_data('../configs/apiConfig.yml'))