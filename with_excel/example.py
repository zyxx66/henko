import create_graph
example = create_graph.create_graph('D:/example_excel.xlsx', 'Sheet1')
# エクセルファイルをロードする
excel_file = example.load()
# 散布図を作る
example.create_scatter(excel_file,'横軸タイトル','横軸タイトル','グラフタイトル','D1',[1,1,1,5,2,1,2,5])
example.create_scatter(excel_file,'横軸タイトル','横軸タイトル','グラフタイトル','L1',[1,1,1,5,2,1,2,5],[1,1,1,5,3,1,3,5])
# エクセルファイル保存
example.save(excel_file)