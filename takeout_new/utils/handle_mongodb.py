# -*- coding: utf-8 -*-
# @File : handle_mongodb.py
# @Time : 2022-07-11 1:33
# @Author : chensiting
# @Email : 475707078@qq.com
# @Software: PyCharm

import pymongo
#创建连接
client=pymongo.MongoClient("mongodb://admin:sq@192.168.131.128:27017/")

#指定数据库
db = client['sq-waimai']

#指定集合
collection = db['categories']

#增加一条数据
# collection.insert_one({"count":10,'level':5,"name":"快餐便当"})

#插入多条数据
mylist = [
    {"count":10,'level':1,"name":"特色菜系"},
    {"count": 20, 'level': 2, "name": "炸鸡"},
    {"count":30,'level':3,"name":"蛋糕"},
    {"count": 40, 'level': 4, "name": "奶茶"}
]
# collection.insert_many(mylist)

#查询
result1 = collection.find_one({"count":301})#返回一个结果  返回是一个字典
print(result1)
#查询返回多个结果
# results2 = collection.find({"name":"蛋糕"})
# print(results2)
# for result in results2:
#     print(result)

#修改操作
# collection.update_one({"count":114},{"$set":{"name":"小吃"}})
# collection.update_many({"count":10},{"$set":{"name":"珍珠"}})

#删除
collection.delete_one({"count":301})#只删除匹配到的一条数据
# collection.delete_many({"count":301})








