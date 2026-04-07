# Creatin a Workbook
import openpyxl as op

workbook = op.Workbook()
sheet = workbook.active
workbook.save('Trial.xlsx')