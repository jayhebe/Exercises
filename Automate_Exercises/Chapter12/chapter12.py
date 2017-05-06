import openpyxl

wb = openpyxl.load_workbook("example.xlsx")
# print(type(wb))
print(wb.get_sheet_names())