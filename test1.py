import os

import openpyxl
import csv


folder = 'C://Users/qq914/Desktop/123/'
f = open(folder+'sumup.csv','a')
file_list = []
result = []
for file in os.listdir(folder):
    if '.csv' in file:
        file_list.append(file)
with open(folder+'2022-11-08-n.csv','r') as ff:
    for k in ff:
        if ',,' in k:
            f.write(k)
