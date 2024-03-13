# -*- coding: utf-8 -*-
# @File : handle_mysql.py
# @Time : 2022-07-10 23:00
# @Author : chensiting
# @Email : 475707078@qq.com
# @Software: PyCharm

import pymysql

#1-创建连接
db = pymysql.connect(host='192.168.131.128',port=3306,
                     user='root',passwd='sq',database='sq-waimai')
#2-获取游标
cursor = db.cursor()

#3-执行sql语句
# cursor.execute('select version();')
#
# #4-获取返回结果
# result1 = cursor.fetchone() #获取返回结果 返回一条结果      ('5.7.31',) 是元组，不可更改
# print(result1)

sql = 'select * from t_cms_contacts;'
cursor.execute(sql)
#4-获取返回结果
result2 = cursor.fetchall() #获取所有结果cursor.fetchall() 返回元组套元组
for one in result2:
    print(one)

#增加操作
# sql= "insert into t_cms_contacts(email,mobile,remark,user_name)values('tese1@qq.com',13800138000,'测试11','李四')"
# cursor.execute(sql)
# # #除了查询操作，其他操作都需要commit一下，才可以同步到数据库
# db.commit()

#修改操作
# sql = 'update t_cms_contacts set mobile="15800000000" where id="7";'
# cursor.execute(sql)
# db.commit()

#删除操作
# sql = 'delete from t_cms_contacts where id="8";'
# cursor.execute(sql)
# db.commit()

#回滚
# sql1 = 'select id,remark from t_cms_contacts where id="1";'
# cursor.execute(sql1)
# result2 = cursor.fetchall()
# for one in result2:
#     print(f'未修改前该行数据:{one}')
#
# #对该行数据进行修改
# sql = 'update t_cms_contacts set remark="测试回滚" where id="1";'
# cursor.execute(sql)
#
# sql1 = 'select id,remark from t_cms_contacts where id="1";'
# cursor.execute(sql1)
# result2 = cursor.fetchall()
# for one in result2:
#     print(f'该行数据修改后的结果:{one}')
#
# db.rollback()
# db.commit()
# sql1 = 'select id,remark from t_cms_contacts where id="1";'
# cursor.execute(sql1)
# result2 = cursor.fetchall()
# for one in result2:
#     print(f'输出事务回滚的结果:{one}')

#5-关闭游标 关闭连接
# cursor.close()
# db.close()
