

def write_file(filepath, content):
    """
        方法名：文件写入
        参数：
            filepath: 文件的路径
            content：要入的内容
        返回值：空
    """
    with open(file=filepath, mode='w', encoding='utf-8') as f:
        f.write(content)


def read_file(filepath):
    """
        方法名：文件读取
        参数：
            filepath：文件的路径
        返回值：返回文件的内容，类型为str
    """
    with open(file=filepath, mode='r', encoding='utf-8') as f:
        result = f.readline()

    return result
