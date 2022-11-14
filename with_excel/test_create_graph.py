import openpyxl
import os
import openpyxl.chart


# 散布図を作る　メソッド
class Create_Graph:
    def __init__(self, file_name: str, sheet_name: str, chart_x_title: str, chart_y_title: str,
                 chart_title: str, chart_place: str, *data_in: list):
        # ⓪file_name　：　読み込むファイルの名
        # ①sheet_name　：　処理したいシートの名
        # ②chart_x_title　：　作成するグラフ横軸のタイトル
        # ③chart_y_title　：　作成するグラフ縦軸のタイトル
        # ④chart_title
        # ⑤chart_place
        # ⑥data_in　：　グラフのデータ
        # ⑦data_in = [
        #            ⓪　x_x1 ,① x_y1 ,② x_x2 ,③ x_y2 ,
        #               横軸のデータ (x_x1,x_y1) ~ (x_x2,x_y2)
        #            ④　y_x1 ,⑤ y_y1 ,⑥ y_x2 ,⑦ y_y2 ,
        #               縦軸のデータ (y_x1,y_y1) ~ (y_x2,y_y2)
        #            ]
        self.file_name = file_name
        self.sheet_name = sheet_name
        self.chart_x_title = chart_x_title
        self.chart_y_title = chart_y_title
        self.data_in = data_in
        self.chart_title = chart_title
        self.chart_place = chart_place

    def create_scatter(self):
        series = []
        # エクセルファイルを読み込む
        work_book = openpyxl.load_workbook(self.file_name)
        # 編集したいシートを指定する
        work_sheet = work_book[self.sheet_name]
        k = 0
        for i in range(len(self.data_in)):
            x_data = openpyxl.chart.Reference(work_sheet, self.data_in[i][0], self.data_in[i][1],
                                              self.data_in[i][2], self.data_in[i][3])
            y_data = openpyxl.chart.Reference(work_sheet, self.data_in[i][4], self.data_in[i][5],
                                              self.data_in[i][6], self.data_in[i][7])
            series.append(openpyxl.chart.Series(y_data, x_data, title_from_data=False))

        chart = openpyxl.chart.ScatterChart()
        chart.title = self.chart_title
        chart.style = 10
        chart.y_axis.title = self.chart_y_title
        chart.x_axis.title = self.chart_x_title
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

        work_sheet.add_chart(chart, self.chart_place)
        print('-----------------')
        print('処理完了')
        print('-----------------')

        work_book.save(self.file_name)



def cell(x : str,y : str):


if __name__ == '__main__':
    file = 'C:/Users/zyxx/Desktop/2022-11-09.xlsx'
    sheet_name = 'Sheet1'
    chart_x_title = '角度(°)'
    chart_y_title = '照度'
    chat_title = ''
    chart_place = 'H163'
    x_data = [1,163,1,199,3,163,4,199]
    y_data = [1,163,1,199,4,163,4,199]

    graph = Create_Graph(file,sheet_name,chart_x_title,chart_y_title,chat_title,chart_place,x_data,y_data)

    graph.create_scatter()
