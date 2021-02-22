"""
文章接口测试用例
"""
import requests
import pytest
import os
import sys
sys.path.append(os.getcwd())
from utils.exceltools import read_excel
from utils.dbtools import query
from utils.filetools import read_file
from utils.filetools import write_file

datas = read_excel("data/data1.xlsx","文章")
# def test_01_get_article():  #获取文章详情接口
#     u = datas[0][2]
#     res = requests.get(url=u)
#     assert res.status_code == datas[0][5]
#     assert res.json()["status"] == datas[0][6]

def test_02_new_article():     #用户写文章接口
    u = datas[1][2]
    d = eval(datas[1][3])
    h = eval(datas[1][4])
    res=requests.post(url=u,json=d,headers=h)
    assert res.status_code == datas[1][5]
    assert res.json()["status"] == datas[1][6]
    aid = res.json()['data']['articleid']
    write_file("./temp/aid.txt",str(aid))
    #数据库校验
    sql = "select * from t_article where id={}".format(read_file("./temp/aid.txt"))
    assert len(query(sql)) != 0

def test_03_update_article():   #用户修改文章接口
    u = datas[2][2]
    d = eval(datas[2][3])
    h = eval(datas[2][4])
    res=requests.post(url=u,json=d,headers=h)
    assert res.status_code == datas[2][5]
    assert res.json()["status"] == datas[2][6]
    #数据库校验
    sql="select * from t_article where id={}".format(d["aid"])
    res=query(sql)
    print(res)
    assert int(d["aid"]) in res[0]
    assert d["title"] in res[0]

# def test_04_delete_article():   #用户删除文章接口
#     u = datas[3][2]
#     d = eval(datas[3][3])
#     h = eval(datas[3][4])
#     res=requests.post(url=u,json=d,headers=h)
#     assert res.status_code == datas[3][5]
#     assert res.json()["status"] == datas[3][6]
#     #数据库校验
#     sql = "select * from t_article where id={}".format(d["aid"])
#     res = query(sql)
#     assert len(res) == 0

# def test_05_upload():       #上传图片
#     u = datas[4][2]
#     d = eval(datas[4][3])
#     h = eval(datas[4][4])
#     res = requests.post(url=u,json=d,headers=h)
    
#     try:
#         assert res.status_code == 200
#     except:
#         print("你好")
#     try:
#         assert res.json()["status"] == 200
#     except:
#         print("好的")
#     print(res.text)

# def test_06_like():     #点赞/取消点赞接口
#     u = datas[5][2]
#     d = eval(datas[5][3])
#     h = eval(datas[5][4])
#     res = requests.post(url=u,json=d,headers=h)
#     assert res.status_code == datas[5][5]
#     assert res.json()["status"] == datas[5][6]


   
   