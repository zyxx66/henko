import openpyxl
import openpyxl.chart


# 散布図を作る　メソッド
class create_graph():
    # 定義、create_graph('file_name','sheet_name')で使うように
    def __init__(self, file_name, sheet_name):
        self.file_name = file_name
        self.sheet_name = sheet_name

    #   エクセルファイルを読み込む
    def load(self):
        work_book = openpyxl.load_workbook(self.file_name)
        work_sheet = work_book[self.sheet_name]
        return [work_book, work_sheet]

    def save(self, work_book: list):
        work_book[0].save(self.file_name)

    def create_scatter(self, load_work_book: list, chart_x_title: str, chart_y_title: str,
                       chart_title: str, chart_place: str, *data_in: list):

        series = []
        # 編集したいシートを指定する
        work_sheet = load_work_book[1]
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
