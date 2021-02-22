import requests
from utils.exceltools import read_excel
from utils.filetools import read_file
from utils.dbtools import query

datas = read_excel("data/data1.xlsx","标签列表")
datas2 = read_excel("data/data2.xlsx","标签列表")

# def test_01_gettaglist():       #获取标签列表接口
#     u = datas[0][2]
#     res = requests.get(url=u)
#     assert res.status_code == datas[0][5]
#     assert res.json()["status"] == datas[0][6]

# def test_02_back_gettagslist():     #后台获取标签列表接口
#     u = datas2[0][2]
#     h = eval(datas2[0][4])
#     res = requests.get(url=u,headers=h)
#     assert res.status_code == datas2[0][5]
#     assert res.json()["status"] == datas2[0][6]

# def test_03_newtags():      #后台新增标签列表接口
#     u = datas2[1][2]
#     d = eval(datas2[1][3])  
#     h = eval(datas2[1][4])
#     res = requests.post(url=u,json=d,headers=h)
#     assert res.status_code == datas2[1][5]
#     assert res.json()["status"] == datas2[1][6]
#     #数据库校验
#     sql = "select * from t_content_tags where tags='{}'".format(d["tags"])
#     res = query(sql)
#     print(res)
#     assert res[0][2] == d["tags"]

# def test_04_updatetags():       #后台修改标签列表
#     u = datas2[2][2]
#     d = eval(datas2[2][3])
#     h = eval(datas2[2][4])
#     res = requests.post(url=u,json=d,headers=h)
#     assert res.status_code == datas2[2][5]
#     assert res.json()["status"] == datas2[2][6]
#     #数据库校验
#     sql = "select * from t_content_tags where id=675"
#     res = query(sql)
#     assert res[0][2] == d["tags"]

# def test_05_deletetags():       #后台删除标签列表
#     u = datas2[3][2]
#     d = eval(datas2[3][3])
#     h = eval(datas2[3][4])
#     res = requests.post(url=u,json=d,headers=h)
#     assert res.status_code == datas2[3][5]
#     assert res.json()["status"] == datas2[3][6]
#     #数据库校验
#     sql = "select * from t_content_tags where id=675"
#     res = query(sql)
#     assert len(res) == 0