#!/usr/bin/env python
# coding: utf-8
import os

import xlrd  # 读取excel表

#读取excel测试用例
#file = 'testdata.xlsx'
# file = r'D:\work\FDD\saas\pytest1\pytestDDT\testdata.xlsx' #只能用绝对路径
# workbook = xlrd.open_workbook(file) #打开文件
# print(workbook.sheet_names()) #打印字表名称，返回list,下标获取
# #workSheet = workbook.sheet_names()[1]
# workSheet = workbook.sheet_by_name("Sheet1")
# #读取一行
# rows = workSheet.row_values(2)
# print(rows)
# #读取一列
# cols=workSheet.col_values(1)
# print(cols)
# #读取某个单元格
# cellData=workSheet.cell_value(1,2)
# print(cellData)

def get_data(path,sheetname):
    #打开给定路径的文件
    workbook =xlrd.open_workbook(path)

    #打开给定字表名称的表
    print("当前路径1 -> %s" % os.getcwd())
    workSheet = workbook.sheet_by_name(sheetname)
    sheetdata=[]
    #确定表头
    headers=workSheet.row_values(0) #第一行（表头）
    #获取表头下的数据
    for r in range(1,workSheet.nrows): #nrows获取行数
        row_vars = workSheet.row_values(r) #获取每一行
        tmp_dict={}
        #for i in range(len(headers)): #len获取长度（多少列）
        tmp_dict=dict(zip(headers,row_vars)) #映射函数方式来构造字典
        sheetdata.append(tmp_dict) #将第n个测试用例添加到列表（第n行）
    return sheetdata

#只获取需要的模块的用例
def get_needcase(path,sheetname,module):
    all_data=get_data(path,sheetname)
    test_data=[]
    for data in all_data:
        if data['功能模块']==module:
            test_data.append(data)
    return test_data

# path=r'D:\work\FDD\saas\pytest1\pytestDDT\testdata.xlsx'
# sheetname='Sheet1'
# testcase=get_data(path,sheetname)
# print(testcase)
# print(len(testcase))





