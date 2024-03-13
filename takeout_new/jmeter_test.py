# -*- coding: utf-8 -*-
# @File : jmeter_test.py
# @Time : 2022-06-22 17:03
# @Author : chensiting
# @Email : 475707078@qq.com
# @Software: PyCharm
from flask import Flask,request,jsonify # 用来把返回数据转化成JSON的
import json
app = Flask(__name__)


@app.route('/',methods=['POST'])
def hello_world():
    data = request.get_data()
    j_data = json.loads(data)
    print(j_data)
    res_data = j_data['my_test']
    msg = {
        "you_data":res_data
    }
    return jsonify(msg)


if __name__ == '__main__':
    app.run(debug=True, port=80)
    print('被调用')