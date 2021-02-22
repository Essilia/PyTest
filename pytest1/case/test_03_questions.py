# """
# 提问接口测试用例
# """
# import pytest
# import requests
# import os
# import sys
# sys.path.append(os.getcwd())
# from utils.exceltools import read_excel
# from utils.dbtools import query
# from utils.filetools import read_file
# from utils.filetools import write_file


# datas = read_excel("data/data1.xlsx", "问题")

# # def test_01_get_question():  # 获取问题详情接口
# #     u = datas[0][2]
# #     res = requests.get(url=u)
# #     assert res.status_code == datas[0][5]
# #     assert res.json()["status"] == datas[0][6]

# def test_01_new_question():  # 新增提问接口
#     u = datas[1][2]  # 用户提问接口地址
#     d = eval(datas[1][3])  # 接口参数
#     h = eval(datas[1][4])  # 请求头
#     res = requests.post(url=u, headers=h, json=d)
#     qid = res.json()["data"]["questionid"]
#     write_file("./temp/qid.txt", str(qid))
#     assert res.status_code == datas[1][5]
#     assert res.json()["status"] == datas[1][6]
#     # 数据库校验
#     sql = "select * from t_questions where id={}".format(
#         read_file("./temp/qid.txt"))
#     qid = query(sql)
#     assert len(qid) != 0

# def test_02_update_question():  # 修改提问接口
#     u = datas[2][2]
#     d = eval(datas[2][3])  # 接口参数
#     h = eval(datas[2][4])  # 请求头
#     res = requests.post(url=u, headers=h, json=d)
#     assert res.status_code == datas[2][5]
#     assert res.json()["status"] == datas[2][6]
#     # 数据库校验
#     # qid
#     sql = "select * from t_questions where id={}".format(d["qid"])
#     res=query(sql)
#     print(res)
#     assert int(d["qid"]) in res[0]
#     assert d["title"] in res[0]
 

# # def test_03_delete_question():  # 修改删除接口
# #     u = datas[3][2]
# #     d = eval(datas[3][3])  # 接口参数
# #     h = eval(datas[3][4])  # 请求头
# #     res = requests.post(url=u, headers=h, json=d)
# #     assert res.status_code == datas[3][5]
# #     assert res.json()["status"] == datas[3][6]
#     # # 数据库校验
#     # sql = "select * from t_questions where id={}".format(d["qid"])
#     # res = query(sql)
#     # assert len(qid) == 0
