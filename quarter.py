import jieba
import xlrd

file_name = "close_door.xls"

def read_excel():
    wb = xlrd.open_workbook(filename=file_name)
    sheet1 = wb.sheet_by_name('查询结果')
    cols = sheet1.col_values(9)
    txt = ''
    for row_txt in cols:
        jlist = jieba.lcut(row_txt)
        print(jlist)
    #     txt += row_txt
    # print(txt)
    # jlist = jieba.lcut(txt)


if __name__ == '__main__':
    read_excel()