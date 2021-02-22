"""
登录的接口测试用例
"""
import pytest
import requests
import os,sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import write_file
from utils.exceltools import read_excel

datas = read_excel("data/data1.xlsx","登录")
datas2 = read_excel("data/data2.xlsx","登录")

def test_01_loginsuccess():     #登录成功接口
    u = datas[0][2]
    d = eval(datas[0][3])
    h = eval(datas[0][4])
    res = requests.post(url=u,headers=h,json=d)
    write_file("./temp/user_token.txt",res.json()["data"]["token"])
    assert res.status_code == datas[0][5]
    assert res.json()["status"] == datas[0][6]
    #数据库校验
    sql = "select * from t_user where username='{}'".format(d["username"])
    assert len(query(sql)) !=0
    print("测试登录成功")

# def test_02_loginfail():        #登录失败接口
#     u = datas[1][2]
#     d = eval(datas[1][3])
#     h = eval(datas[1][4])
#     res = requests.post(url=u,headers=h,json=d)
#     assert res.status_code == datas[1][5]
#     assert res.json()["status"] == datas[1][6]

# def test_03_adminlogin():       #后台登录成功接口
#     u = datas2[0][2]
#     d = eval(datas2[0][3])
#     h = eval(datas2[0][4])
#     res = requests.post(url=u,headers=h,json=d)
#     write_file("./temp/admin_token.txt",res.json()["data"]["token"])
#     assert res.status_code == datas2[0][5]
#     assert res.json()["status"] == datas2[0][6]
#     #数据库校验
#     sql = "select * from t_user where username='{}'".format(d['username'])
#     res = query(sql)
#     assert len(res) != 0



