import openpyxl
import os

workbook = openpyxl.load_workbook('C:/Users/zyxx/Desktop/2022-11-08.xlsx')
sheet = workbook.active

# print(sheet.cell(3,3).value)
# sheet.cell(3,3).value = 6


sheet.cell(16,16).value = sheet.cell(2,16).value
for k in range(21):
    for i in range(6):
        sheet.cell(16+i,15+2*k).value = sheet.cell(2+i,16+k).value
        sheet.cell(16+i,16+2*k).value = sheet.cell(9+i,16+k).value

workbook.save('C:/Users/zyxx/Desktop/2022-11-08.xlsx')