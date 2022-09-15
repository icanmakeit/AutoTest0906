import xlrd2

book = xlrd2.open_workbook("testdata.xls")
sheet = book.sheet_by_index(0)
rows = sheet.nrows
cols = sheet.ncols


for i in range(rows):
    v_values = sheet.row_values(i)
    print(v_values)


for i in range(cols):
    c_values = sheet.col_values(i)
    print(c_values)

print(sheet.cell(1, 1))
