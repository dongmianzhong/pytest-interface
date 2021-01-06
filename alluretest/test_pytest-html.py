
import pytest
import requests
import json
import pytest_html
import time

class TestAnnouncement():
    def test_add_announcement(self):
        baseurl = 'http://test-mesh.fangdd.net'

        header = {
            'host': 'org.saas.ap.fdd',
            'content-type': 'application/json',
            'User-Id': '3023300'
        }

        Data = {
            "author": "发布人",
            "isTop": 1,
            "mainText": "内allu容",
            "summaryText": "摘要",
            "title": "标allure题"
        }
        r = requests.post(baseurl + '/announcement/add', headers=header,
                          data=json.dumps(Data))  # 字典转换成json字符串，requests换回的是对象
        # rs=json.loads(r.text)
        # print(rs)
        # print(r.json())
        rs = r.json()  # 返回对象的json，返回对象包含返回头、返回码等等
        print(rs['msg'])
        assert True


if __name__ == '__main__':
    NowTime = int(time.time())
    html = '--html='+'pytest-html-report/'+'report' + str(NowTime) + '.html'
    pytest.main([html, '--self-contained-html', 'test_pytest-html.py'])
    # cmd命令：pytest -v -s --html=report.html --self-contained-html test_pytest-html.py
    # pytest.main 需要在python运行，不能在pytest下运行（不会生成测试报告）
