import openpyxl
file = 'C:/Users/zyxx/Desktop/2022-11-22.xlsx'

wb = openpyxl.load_workbook(file)
ws = wb.active


for i in range(22):
    ws.cell(29,3*i+2).value =str(650+i*50)
    for k in range(7):
        # ws.cell(30,2).value = ws.cell(3,2).value
        # ws.cell(30,3).value = ws.cell(3,3).value
        #
        # ws.cell(31,2).value = ws.cell(3,5).value
        # ws.cell(31,3).value = ws.cell(3,6).value
        #
        # ws.cell(30,5).value = ws.cell(4,2).value
        # ws.cell(30,6).value = ws.cell(4,3).value

        ws.cell(30+k,2+i*3).value = ws.cell(3+i,2+k*3).value
        ws.cell(30+k,3+i*3).value = ws.cell(3+i,3+3*k).value

wb.save(file)