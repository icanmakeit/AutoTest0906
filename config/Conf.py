import os
from utils.YamlUtil import YamlReader

current = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(current))

_config_path = BASE_DIR + os.sep + "config"
_config_file = _config_path + os.sep + "conf.yaml"
_log_path = BASE_DIR + os.sep + "logs"

# 定义data目录的路径
_data_path = BASE_DIR + os.sep + "data"

# 定义report目录的路径
_report_path = BASE_DIR + os.sep + "report"


def get_report_path():
    """获取report绝对路径"""
    return _report_path


def get_data_path():
    return _data_path


def get_config_path():
    return _config_path


def get_config_file():
    return _config_file


def get_log_path():
    return _log_path


class ConfigYaml:
    def __init__(self):
        self.config = YamlReader(get_config_file()).data()

    def get_excel_file(self):
        return self.config["BASE"]["test"]["case_file"]

    def get_excel_sheet(self):
        return self.config["BASE"]["test"]["case_sheet"]

    def get_conf_url(self):
        return self.config["BASE"]["test"]["url"]

    def get_conf_log(self):
        return self.config["BASE"]["log_level"]

    def get_conf_log_extension(self):
        return self.config["BASE"]["log_extension"]

    def get_email_info(self):
        """获取邮件配置相关信息"""
        return self.config["email"]


if __name__ == '__main__':
    conf_read = ConfigYaml()
    print(conf_read.get_conf_url())
    print(conf_read.get_conf_log())
    print(conf_read.get_conf_log_extension())
    print(conf_read.get_email_info())

    print(_report_path)
    print(get_report_path() + os.sep + "result")



