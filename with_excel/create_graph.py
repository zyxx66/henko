import openpyxl
import os
import openpyxl.chart


# 散布図を作る　メソッド

def create_scatter(file_name: str, sheet_name: str, chart_x_title: str, chart_y_title: str,
             chart_title: str, chart_place: str, *data_in: list):
    series = []
    # エクセルファイルを読み込む
    work_book = openpyxl.load_workbook(file_name)
    # 編集したいシートを指定する
    work_sheet = work_book[sheet_name]
    k = 0
    for i in range(len(data_in)):
        x_data = openpyxl.chart.Reference(work_sheet, data_in[i][0], data_in[i][1],
                                          data_in[i][2], data_in[i][3])
        y_data = openpyxl.chart.Reference(work_sheet, data_in[i][4], data_in[i][5],
                                          data_in[i][6], data_in[i][7])
        series.append(openpyxl.chart.Series(y_data, x_data, title_from_data=False))

    chart = openpyxl.chart.ScatterChart()
    chart.title = chart_title
    chart.style = 10
    chart.y_axis.title = chart_y_title
    chart.x_axis.title = chart_x_title
    for i in range(series.__len__()):
        series[i].marker.symbol = 'circle'
        if i == 0:
            series[i].marker.graphicalProperties.solidFill = '0066FF'
            series[i].marker.graphicalProperties.line.solidFill = '0066FF'
        elif i == 1:
            series[i].marker.graphicalProperties.solidFill = 'FF9900'
            series[i].marker.graphicalProperties.line.solidFill = 'FF9900'

        series[i].graphicalProperties.line.noFill = True
        chart.append(series[i])

    work_sheet.add_chart(chart, chart_place)
    print('-----------------')
    print('処理完了')
    print('-----------------')

    work_book.save(file_name)


if __name__ == '__main__':
    file = 'C:/Users/zyxx/Desktop/2022-11-09.xlsx'
    sheet_name = 'Sheet1'
    chart_x_title = '角度(°)'
    chart_y_title = '照度'
    chat_title = ''
    chart_place = 'H163'
    x_data = [1, 163, 1, 199, 3, 163, 4, 199]
    y_data = [1, 163, 1, 199, 4, 163, 4, 199]

    graph = Create_Graph(file, sheet_name, chart_x_title, chart_y_title, chat_title, chart_place, x_data, y_data)

    graph.create_scatter()
