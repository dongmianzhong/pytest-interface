#!/usr/bin/env python
# coding: utf-8
import json
import os
import requests
import pytest
# import allure

from readexcel import get_needcase


def testing(baseurl,case):
    header=case['请求头']
    body=case['请求参数'].encode('utf-8')
    # print('body****')
    # print(body)
    url=case['请求url']
    print(case['功能模块']+'---'+case['功能']+'----'+case['描述'])

    if case['调用方法']=='POST':
        r = requests.post(baseurl + url, headers=json.loads(header), data=body)
        return r.json()
    if case['调用方法']=="GET":
        r=requests.get(baseurl+url,headers=json.loads(header),params=json.loads(body))
        # print('***')
        # print(r.url)
        return r.json()


# class test_Ann():
#     from readexcel import get_needcase
#     path = 'testdata.xlsx'
#     sheetname = 'Sheet1'
#     module = '公司公告'
#     baseurl = 'http://test-mesh.fangdd.net'
#     test_case = get_needcase(path, sheetname, module)
#     @pytest.mark.parametrize('case', test_case)
#     def test_Announcement(case):
#         result = testing(baseurl, case)
#         actual_msg = result['msg']
#         actual = f'{{"msg":"{actual_msg}"}}'
#         expect = case['断言']
#         assert actual == expect


path = './pytestDDT/testdata1.xls'
sheetname='Sheet1'
module='公司公告'
baseurl = 'http://test-mesh.fangdd.net'
test_case=get_needcase(path, sheetname, module)
@pytest.mark.parametrize('case',test_case)
def test_Announcement(case):
    result=testing(baseurl,case)
    actual_msg = result['msg']
    actual=f'{{"msg":"{actual_msg}"}}'
    expect=case['断言']
    assert actual==expect

# if __name__=='__main__':
#     pytest.main(['-v', '-s', 'ddt.py'])

# if __name__=='__main__':
#     path = 'pytestDDT/testdata.xlsx'
#     sheetname='Sheet1'
#     module='公司公告'
#     baseurl = 'http://test-mesh.fangdd.net'
#
#     test_case=get_needcase(path, sheetname, module)
#     print('----测试用例----')
#     print(test_case)
#     for case in test_case:
#         print('______调用结果______')
#         result=testing(baseurl,case)
#         # print("******result")
#         # print(json.dumps(result))
#         # Assert=case['断言']
#         # print(Assert)
#         # assert result['msg']==Assert
#         # print("结束")
#         actual_msg=result['msg']
#         actual=f'{{"msg":"{actual_msg}"}}'
#         expect=case['断言']
#         assert actual==expect







