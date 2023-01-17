import create_graph
example = create_graph.create_graph('D:/example_excel.xlsx', 'Sheet1')
# エクセルファイルをロードする
excel_file = example.load()
# 散布図を作る
example.create_scatter(excel_file,'横軸タイトル１','横軸タイトル１','グラフタイトル１','D1',[[1,1,1,5,2,1,2,5,'例１']])
example.create_scatter(excel_file,'横軸タイトル２','横軸タイトル２','グラフタイトル２','L1',[[1,1,1,5,2,1,2,5,'なんでも'],[1,1,1,5,3,1,3,5,'いいですよ']])
# エクセルファイル保存
example.save(excel_file)