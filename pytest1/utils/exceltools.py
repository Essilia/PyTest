"""
    读取excel
"""
import xlrd

def read_excel(excel_path, sheet_name, skip_first=True):
    results = []
    datas = xlrd.open_workbook(excel_path)
    table = datas.sheet_by_name(sheet_name)
    if skip_first == True:
        start_row = 1
    else:
        start_row = 0

    # 循环读取每一行的数据
    for row in range(start_row, table.nrows): #(0, 1)
        results.append(table.row_values(row))

    return results


# r = read_excel("data\data.xlsx", "首页")
# print(r)


