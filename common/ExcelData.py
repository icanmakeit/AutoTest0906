from utils.ExcelUtil import ExcelReader
from common.ExcelConfig import DataConfig


class Data:
    def __init__(self, testcase_file, sheet_name):
        self.reader = ExcelReader(testcase_file, sheet_name)
        print(self.reader.data())

    def get_run_data(self):
        """是否运行"""
        run_list = list()
        for line in self.reader.data():
            if str(line[DataConfig().is_run]).lower() == "y":
                run_list.append(line)
        return run_list

    def get_case_list(self):
        """获取全部测试用例"""
        run_list = list()
        for line in self.reader.data():
            run_list.append(line)
        return run_list

    def get_case_pre(self, pre):
        """根据前置条件获取对应的用例"""
        run_list = self.get_case_list()
        for line in run_list:
            if pre in dict(line).values():
                return line
        return None
