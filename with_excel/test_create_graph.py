import openpyxl
import os
import openpyxl.chart


# 散布図を作るクラスである
# file_name：
#
# sheet_name:
#
# data_from:データ範囲
# data_from = [1,1,5,4] ： ( [A1:E4]　のデータをグラフにする)
# graph_to：グラフの位置
# graph_to = F6　： (出来上がったグラフを　F6　に置く)
class data:
    def __init__(self, x_data, y_data, graph_to, ):
        return [x_data, y_data, graph_to]


class Create_Graph:
    def __init__(self, file_name: str, sheet_name: str, chart_x_title, chart_y_title, *data_in):
        self.file_name = file_name
        self.sheet_name = sheet_name
        self.chart_x_title = chart_x_title
        self.chart_y_title = chart_y_title
        self.data = data_in

    def create_scatter(self):
        # エクセルファイルを読み込む
        work_book = openpyxl.load_workbook(self.file_name)
        # 編集したいシートを指定する
        work_sheet = work_book[self.sheet_name]
        k = 0
        for i in self.data:
            x_data = openpyxl.chart.Reference(work_sheet, self.x_data_from[0], self.x_data_from[1], self.x_data_from[2],
                                              self.x_data_from[3])
            y_data = openpyxl.chart.Reference(work_sheet, self.y_data_from[0], self.y_data_from[1], self.y_data_from[2],
                                              self.y_data_from[3])
            series = openpyxl.chart.Series(y_data, x_data, title_from_data=False)

        chart = openpyxl.chart.ScatterChart()
        chart.title = self.chart_name
        chart.style = 10
        chart.y_axis.title = self.chart_y_title
        chart.x_axis.title = self.chart_x_title
        series.marker.symbol = 'circle'
        series.marker.graphicalProperties.solidFill = '0066FF'
        series.marker.graphicalProperties.line.solidFill = '0066FF'
        series.graphicalProperties.line.noFill = True

        chart.append(series)

        work_sheet.add_chart(chart, self.graph_to)
        print('-----------------')
        print('処理完了')
        print('-----------------')

        work_book.save(self.file_name)


file = 'C:/Users/zyxx/Desktop/2022-11-09.xlsx'
row_start = 163
row_end = 199
x_data_column = 1
y_data_column = 2
chart_name = ['test', 'test_x', 'test_y']

graph = Create_Graph(file, 'Sheet1',
                     [x_data_column, row_start, x_data_column, row_end],
                     [y_data_column, row_start, y_data_column, row_end],
                     chart_name, 'H163'
                     )
graph.create_scatter()
