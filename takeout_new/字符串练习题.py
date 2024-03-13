# -*- coding: utf-8 -*-
# @File : 字符串练习题.py
# @Time : 2022-07-21 18:01
# @Author : chensiting
# @Email : 475707078@qq.com
# @Software: PyCharm
print()
'''
1、已知 a 的值为 "hello"，b 的值为 "world"，如何交换 a 和 b 的值？
得到 a 的值为 "world"，b 的值为 "hello"
'''
# a = "hello"
# b = "world"
# # c = a
# # a= b
# # print(a)
# # b=c
# # print(b)
# a,b =b,a
# print(a,b)
'''
2.回文的定义： "回文"就是正读倒读都一样的。
如奇数个： "98789" ，这个数字正读是"98789" 倒读也是"98789"。
偶数个数字"3223"也是回文数。
字母 "abcba" 也是回文。
判断一个字符串是否是回文字符串，是打印True， 不是打印False
'''
# a = "98711789"
# if a == a[::-1]:
#     print(True)
# else:
#     print(False)
# a = "98711789"
# print(reversed(a))
# print("".join(reversed(a)))
# print(a == "".join(reversed(a)))

'''
3.1已知一个字符串为"hello_world_yoyo", 
如何得到一个队列 ["hello", "world", "yoyo"]

3.2让用户输入任意的用户名与密码，然后将他输入的用户名与密码打印出来，如用户输入 abc/123 ，则打印
您输入的用户名是: abc 
密码是:123

'''
# a = "hello_world_yoyo"
# print(a.split("_"))

# into = input("请输入用户名与密码（格式user/password）：")
# name = into.split("/")[0]
# password=into.split("/")[-1]
# print("您输入的用户名是",name)
# print("您输入的用户名是",password)

'''
4.
有个列表 ["hello", "world", "yoyo"]
如何把把列表里面的字符串联起来，
得到字符串 "hello_world_yoyo"
'''
# a=["hello", "world", "yoyo"]
# print("_".join(a))
'''

5.把字符串 s 中的每个空格替换成"%20"
输入：s = "We are happy."
输出："We%20are%20happy."
'''
# s = "We are happy."
# print(s.replace(" ","%20"))
'''
6.99乘法表
'''
#
# for i in range(1,10):
#     # print('行数',i)
#     for j in range(1,i+1):
#         # print('列数',i)
#         print('%s*%s =%-2s' %(j,i,j*i),end='  ')    #%-2s 左对齐
#     print() #本身有换行的效果
'''
7.找出单词 “welcome” 在 字符串“Hello, welcome to my world.” 中出现的位置，找不到返回-1
从下标0开始索引
'''
# a= 'Hello, welcome to my world.'
#
# if 'welcome' in a:
#     print(a.index('welcome'))
# else:
#     print(-1)
'''
8.统计字符串“Hello, welcome to my world.” 中字母w出现的次数
统计单词 my 出现的次数

'''
# a='Hello, welcome to my world.'
# print(a.count('w'))
# print(a.count('my'))
'''
9.输入一个字符串 str, 输出第 m 个只出现过 n 次的字符，如在字符串 gbgkkdehh 中,
找出第2个只出现1 次的字符，输出结果：d
'''
# from collections import Counter
# a='gbgkkdehh'
# b=Counter(a)
# n=1
# m=2
# # print(dict(b))
# s=[]
# for i,j in dict(b).items():
#     print(i,j)
#     if j==n:
#         s.append(i)
# print(s)
# print(s[m-1])
'''
10.判断字符串a="welcome to my world" 是否包含单词b="world"
包含返回True，不包含返回 False
'''
a="welcome to my world"
b="wo4rld"
if b in a:
    print(True)
else:
    print(False)



