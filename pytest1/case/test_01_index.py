# """
# 首页的接口测试用例
# """
# import pytest
# import requests
# import os
# import sys
# sys.path.append(os.getcwd())
# from utils.exceltools import read_excel

# datas = read_excel("data/data1.xlsx","首页")

# def test_01_lbt():  # 获取首页轮播图接口
#     u=datas[0][2]
#     res=requests.get(url=u)
#     assert res.status_code == datas[0][5]  # http状态码判断
#     assert res.json()["status"] == datas[0][6]  # 结果码判断

# def test_02_get_coures():  # 获取推荐教程接口
#     u=datas[0][2]
#     res=requests.get(url=u)
#     assert res.status_code == datas[0][5]
#     assert res.json()["status"] == datas[0][6]

# def test_03_get_questions():  # 获取热门讨论
#     u=datas[0][2]
#     res=requests.get(url=u)
#     assert res.status_code == datas[0][5]
#     assert res.json()["status"] == datas[0][6]

# def test_04_get_article():
#     u=datas[0][2]
#     res=requests.get(url=u)
#     assert res.status_code == datas[0][5]
#     assert res.json()["status"] == datas[0][6]


# def test_04_get_inspired():
#     u=datas[0][2]
#     res=requests.get(url=u)
#     assert res.status_code == datas[0][5]
#     assert res.json()["status"] == datas[0][6]


# def test_04_get_highuserds():
#     u=datas[0][2]
#     res=requests.get(url=u)
#     assert res.status_code == datas[0][5]
#     assert res.json()["status"] == datas[0][6]
