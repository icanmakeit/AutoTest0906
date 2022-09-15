import os
import xlrd2


class SheetTypeError:
    pass


class ExcelReader:
    def __init__(self, excel_file,  sheet_by):
        if os.path.exists(excel_file):
            self.excel_file = excel_file
            self.sheet_by = sheet_by
            self._data = list()
        else:
            raise FileNotFoundError("文件不存在")

    def data(self):
        if not self._data:
            workbook = xlrd2.open_workbook(self.excel_file)
            if type(self.sheet_by) not in [str, int]:
                raise SheetTypeError("请输入Int or Str")
            elif type(self.sheet_by) == int:
                sheet = workbook.sheet_by_index(self.sheet_by)
            elif type(self.sheet_by) == str:
                sheet = workbook.sheet_by_name(self.sheet_by)

            title = sheet.row_values(0)
            for col in range(1, sheet.nrows):
                col_value = sheet.row_values(col)
                print(zip(title, col_value))
                print(dict(zip(title, col_value)))
                self._data.append(dict(zip(title, col_value)))
        return self._data


if __name__ == '__main__':
    reader = ExcelReader("../testcase/t_excel/testdata.xls", 0)
    print(reader.data())





