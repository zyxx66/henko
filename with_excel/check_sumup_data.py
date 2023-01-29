# 毎日のデータをまとめたファイルをグラフ化するプログラムである
import csv
import openpyxl

folder = 'F:/daily/result/'
file = 'sumup.csv'

work_sheet = openpyxl.Workbook().active
sum_up_list = []
with open(folder+file) as open_csv_file:
    for row in csv.reader(open_csv_file):
        sum_up_list.append(row)

print(sum_up_list)