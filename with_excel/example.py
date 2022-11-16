import create_graph

example = create_graph.create_graph('D:/example_excel.xlsx', 'Sheet1')
# エクセルファイルをロードする
example.load()

example.create_scatter()
