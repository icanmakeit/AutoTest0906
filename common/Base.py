import json
import logging
from config.Conf import ConfigYaml
import re
import subprocess
from utils.LogUtil import my_log
from utils.EmailUtil import SendEmail

p_data = "\${(.*)}\$"
log = my_log()


def res_find(data, pattern_data=p_data):
    """正则表达式查询指定内容"""
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    return re_res


def res_sub(data, replace, pattern_data=p_data):
    """替换"""
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    if re_res:
        return re.sub(pattern_data, replace, data)
    return re_res


def params_find(headers, cookies):
    """"""
    pass


def json_parse(data):
    return json.loads(data) if data else data


def allure_report(report_path, report_html):
    allure_cmd = "allure generate %s -d %s --clean" % (report_path, report_html)
    try:
        subprocess.call(allure_cmd, shell=True)
    except:
        log.error("执行用例失败，请检查以下测试环境相关配置")
        raise


def send_mail(report_html_path="", content="", title="测试"):
    """发送邮件"""
    email_info = ConfigYaml().get_email_info()
    smtp_addr = email_info["smtpserver"]
    username = email_info["username"]
    password = email_info["password"]
    recv = email_info["receiver"]
    email = SendEmail(
        smtp_addr=smtp_addr,
        username=username,
        password=password,
        recv=recv,
        title=title,
        content=content,
        file=report_html_path
    )
    email.send_mail()


if __name__ == '__main__':
    print(res_find('{"Authorization": "JWT ${token}$"}'))
    print(res_sub('{"Authorization": "JWT ${token}$"}', '123'))
