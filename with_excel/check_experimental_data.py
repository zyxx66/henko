# 実験空得られたデータのグラフｗｐ作成するプログラムである。
# フォルダ(folder)の中にあるcsvファイルをすべて処理する

# 動作:なし

import os
import openpyxl
import csv
import with_excel.create_graph as cg


def check(folder):
    if not os.path.exists(folder + 'excel'):
        os.mkdir(folder + 'excel')

    # すべてのcsvファイル名前をfile_listに入れる
    file_list = []

    for file in os.listdir(folder):
        if '.csv' in file and '-' in file:
            file_list.append(file)

    for csv_name in file_list:
        wb = openpyxl.Workbook()
        ws = wb.active
        csv_file = folder + csv_name
        xlsx_file = folder + 'excel/' + csv_name.split('.')[0] + '.xlsx'

        with open(csv_file, 'r') as f:
            for row in csv.reader(f):
                ws.append(row)

        data = []
        with open(csv_file) as f:
            for row in f:
                data.append(row)

        data_address = []
        check = 0
        start_point = 0

        for i in range(data.__len__()):
            if 'CH0' in data[i]:
                start_point = i + 2
                if check == 0:
                    check = 1
            if '180,' in data[i]:
                check = 0
                data_address.append([start_point, i + 1])

        for k in data_address:
            for i in range(k[0], k[1] + 1):
                for j in range(1, 7):
                    ws.cell(i, j).data_type = 'float'
                    print('123')


        wb.save(xlsx_file)

        graph = cg.create_graph(xlsx_file, 'Sheet')

        for k in data_address:

            if k == data_address[0]:
                load_file = graph.load()
                print('load')

            graph.create_scatter(load_file, '角度', '照度', '偏光' + '(' + data[k[0] - 3].split(',')[3].split('\n')[0] + ')',
                                 'H' + str(k[0]),
                                 [1, k[0], 1, k[1], 2, k[0], 2, k[1]])
            graph.create_scatter(load_file, '角度', '照度', 'ch1 and ch2', 'O' + str(k[0]),
                                 [1, k[0], 1, k[1], 3, k[0], 3, k[1]], [1, k[0], 1, k[1], 4, k[0], 4, k[1]])
            graph.create_scatter(load_file, '角度', '照度', 'lux1 and lux2', 'H' + str(k[0] + 17),
                                 [1, k[0], 1, k[1], 5, k[0], 5, k[1]], [1, k[0], 1, k[1],  6, k[0], 6, k[1]])

            if k == data_address[data_address.__len__() - 1]:
                graph.save(load_file)
                print('save')

    print(data)


if __name__ == '__main__':
    folder = 'C://Users/zyxx/Desktop/test_csv/'
    check(folder)
