import create_graph as cg
xlsx_file = 'C:/Users/zyxx/Desktop/sumup_2.xlsx'
graph = cg.create_graph(xlsx_file, 'sumup_2')

for i in range(24):
    graph.create_scatter(graph.load(),'雲量(％)','照度(Lux)','','B'+str(94+i*5),[3+3*i,30,3+3*i,93,2+3*i,30,2+3*i,93])

graph.save(graph.load())