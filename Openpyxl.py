import openpyxl as op

workbook = op.Workbook()
sheet = workbook.active


sheet['A1'] = "ID"
sheet['B1'] = "Last Name"
sheet['C1'] = "First Name"
sheet['D1'] = "Middle Name"
sheet['E1'] = "Birthyear"
sheet['F1'] = "Age"

workbook.save("excelDB.xlsx")
