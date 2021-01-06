import allure
import pytest
import requests
import json
import time


@allure.feature("公告模块")
class TestAnnouncement():

    @allure.story("添加公告接口")
    def test_add_announcement(self):
        with allure.step("步骤一：参数准备"):
            baseurl = 'http://test-mesh.fangdd.net'

            header = {
                'host': 'org.saas.ap.fdd',
                'content-type': 'application/json',
                'User-Id': '3023300'
            }

            Data = {
                "author": "发布人",
                "isTop": 1,
                "mainText": "allure测试报告",
                "summaryText": "摘要",
                "title": "allure测试报告数据"
            }

        with allure.step("步骤二：接口请求"):
            r = requests.post(baseurl + '/announcement/add', headers=header,
                              data=json.dumps(Data))  # 字典转换成json字符串，requests换回的是对象
            # rs=json.loads(r.text)
            # print(rs)
            # print(r.json())
            rs = r.json()  # 返回对象的json，返回对象包含返回头、返回码等等
            print(rs['msg'])
        with allure.step("步骤三：断言"):
            assert False

    @allure.story("公告列表接口")
    def test_announcement_list(self):
        baseurl = 'http://test-mesh.fangdd.net'

        header = {
            'host': 'org.saas.ap.fdd',
            'content-type': 'application/json',
            'User-Id': '3023300'
        }

        Data = {
            "pageNo": "1",
            "pageSize": "4"
        }
        r = requests.post(baseurl + '/announcement/list', headers=header,
                          data=json.dumps(Data))  # 字典转换成json字符串，requests换回的是对象
        # rs=json.loads(r.text)
        # print(rs)
        # print(r.json())
        rs = r.json()  # 返回对象的json，返回对象包含返回头、返回码等等
        print(rs['msg'])
        assert True


if __name__ == '__main__':
    NowTime = int(time.time())
    alluredir = '--alluredir=' + 'allure-report/' + 'report' + str(NowTime)
    pytest.main(['-s', '-q', alluredir, 'test_allure.py'])

    # cmd命令：pytest test_allure.py -s -q --alluredir=allure-report 生成json文件；
    # 然后
    # 方法一：allure serve ./allure-report 启动网页本地服务在线查看（直接打开默认浏览器）
    # 方法二：从结果生成报告，启动tomcat服务：两个步骤1、生成报告；2、打开报告
    #
    # pytest.main 需要在python运行，不能在pytest下运行（不会生成测试报告）
