# import requests
# import os
# import sys
# sys.path.append(os.getcwd())
# from utils.dbtools import query
# from utils.exceltools import read_excel
# from utils.filetools import read_file

# datas = read_excel("data/data1.xlsx","评论")

# def test_01_get_comments():         #评论列表接口
#     u = datas[0][2]
#     d = eval(datas[0][3])
#     h = eval(datas[0][4])
#     res = requests.post(url=u,json=d,headers=h)
#     assert res.status_code == datas[0][5]
#     assert res.json()["status"] == datas[0][6]

# def test_02_new_comment():          #评论接口
#     u = datas[1][2]
#     d = eval(datas[1][3])
#     h = eval(datas[1][4])
#     res = requests.post(url=u,json=d,headers=h)
#     assert res.status_code == datas[1][5]
#     assert res.json()["status"] == datas[1][6]
#     #数据库校验
#     # sql=


# # def test_02_update_comment():          #修改评论接口
# #     u = datas[2][2]
# #     d = eval(datas[2][3])
# #     h = eval(datas[2][4])
# #     res = requests.post(url=u,json=d,headers=h)
# #     assert res.status_code == datas[2][5]
# #     assert res.json()["status"] == datas[2][6]

# # def test_02_new_comment():          #删除评论接口
# #     u = datas[3][2]
# #     d = eval(datas[3][3])
# #     h = eval(datas[3][4])
# #     res = requests.post(url=u,json=d,headers=h)
# #     assert res.status_code == datas[3][5]
# #     assert res.json()["status"] == datas[3][6]