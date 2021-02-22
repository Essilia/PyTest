import pymysql
# 数据库连接信息
DBCONFIG = {
    "host":"118.24.255.132",
    "port":3306,
    "user":"testgoup",
    "password":"1qaz!QAZ",
    "db":"ljtestdb"
}

def query(sql):
    """
        方法：python连接并且查询数据库
        参数：
            sql："select * from t_user where id=123"
        返回值：
            ((1, 'liuyun1', 'a12345678', ...), ())
    """
    # 步骤1 连接并且打开对应的数据库
    db = pymysql.connect(host=DBCONFIG['host'], port=DBCONFIG['port'], user=DBCONFIG['user'], password=DBCONFIG['password'], db=DBCONFIG['db'])
    # 步骤2：获取查询窗口：游标
    cur = db.cursor()
    # 步骤3：执行sql语句
    cur.execute(sql)
    # 步骤4：获取对应的结果
    res = cur.fetchall()
    # 步骤5：关闭数据库连接
    db.close()

    # 步骤6：返回所有查询的数据
    return res

# 测试方法是否有bug
# r = query("select * from t_user where username ='liuyun1111'")
# print(r)