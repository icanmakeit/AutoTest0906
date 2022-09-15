import allure
import pytest


import config.Conf
from config.Conf import ConfigYaml
import os
from common.ExcelData import Data
from utils.LogUtil import my_log
from common import ExcelConfig
from utils.RequestsUtil import Request
import json
from common import Base
from utils.AssertUtil import AssertUtil

case_file = os.path.join("../data", ConfigYaml().get_excel_file())
sheet_name = ConfigYaml().get_excel_sheet()
data_init = Data(case_file, sheet_name)
run_list = data_init.get_run_data()

log = my_log()
data_key = ExcelConfig.DataConfig


class TestExcel:
    @pytest.mark.parametrize("case", run_list)
    def test_run(self, case):

        url = ConfigYaml().get_conf_url() + case[data_key.url]
        # print(url)
        case_id = case[data_key.case_id]
        case_model = case[data_key.case_model]
        case_name = case[data_key.case_name]
        pre_exec = case[data_key.pre_exec]
        method = case[data_key.method]
        params = case[data_key.params]
        expect_result = case[data_key.expect_result]
        actual_result = case[data_key.actual_result]
        is_run = case[data_key.is_run]
        headers = case[data_key.headers]
        cookies = case[data_key.cookies]
        code = case[data_key.code]
        db_verify = case[data_key.db_verify]

        # 判断headers是否存在
        if headers:
            header = json.loads(headers)
        else:
            header = headers

        if cookies:
            cookie = json.loads(cookies)
        else:
            cookie = cookies

        # 验证前置条件
        if pre_exec:
            pre_case = data_init.get_case_pre(pre_exec)
            print("前置条件信息为：%s " % pre_case)

        # 接口请求
        request = Request()
        if len(str(params).strip()) is not 0:
            params = json.loads(params)
        if str(method).lower() == "get":
            res = request.get(url, data=params, headers=header, cookies=cookie)
            log.info("GET 请求: 用例编号：%s， 用例名称：%s" % (case_id, case_name))
        elif str(method).lower() == "post":
            res = request.post(url, data=params, headers=header, cookies=cookie)
            log.info("POST 请求: 用例编号：%s， 用例名称：%s" % (case_id, case_name))
        else:
            log.error("错误请求methods: %s" % method)
        # print("case_id:%s============resres=====================%s"%(case_id, res))
        # print("case_id:%s============resres=====================%s"% (case_id, str(res["body"]["msg"])))
        # print("----expect_result------%s"% str(expect_result))

        # allure
        # sheet名称
        allure.dynamic.feature(sheet_name)
        # 模块
        allure.dynamic.story(case_model)
        # 用例ID+ 接口名称
        allure.dynamic.title(case_id + case_name)

        desc = "<font color='red'> </font> {} <Br/>" \
               "<font color='red'> </font> {} <Br/>" \
               "<font color='red'> </font> {} <Br/>" \
               "<font color='red'> </font> {} <Br/>".format(url, method, expect_result, res)
        allure.dynamic.description(desc)

        # 断言验证
        assert_util = AssertUtil()
        # assert_util.assert_code(int(res["code"]), int(code))
        # assert_util.assert_body()
        assert_util.assert_in_body(str(res["body"]["msg"]), str(expect_result))
        # print(str(res["msg"]))


if __name__ == '__main__':
    # pytest.main(["-s", "test_excel_case.py"])
    pytest.main(['-s', "test_excel_case.py", "--alluredir", "./report/result"])

    report_path = config.Conf.get_report_path() + os.sep + "result"
    report_html_path = config.Conf.get_report_path() + os.sep + "html"

    Base.allure_report(report_path, report_html_path)

    # Base.allure_report("./report/result", "./report/html")
    # Base.send_mail(title="接口测试报告结果", content=report_html_path, report_html_path="./allure-report/index.html")
    Base.send_mail(title="接口测试报告结果", content=report_html_path)
