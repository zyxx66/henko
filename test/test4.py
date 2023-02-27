import time
import os
from with_excel import create_graph
xlsx_file = create_graph.create_graph('D://sumup_all .xlsx','時間別')
load = xlsx_file.load()
list1 = []
for i in range(19):
    list1.append([i*2+3,i*2+2])
print(list1)
list2=[[3,18],[19,47],[79,99],[100,130],[131,160],[161,191],[192,220]]
dic = {}
for i in range(19):
    if i%2 == 0:
        dic.update({i:'%i:%s'%(i//2+8,'00')})
    else:
        dic.update({i:'%i:%s'%(i//2+8,'30')})
dic2 = {0:'A',1:'I',2:'Q',3:'Y',4:'AG',5:'AO',6:'AV'}
d = 0
for j in range(list2.__len__()):
    k = 223
    for i in range(19):
        xlsx_file.create_scatter(load,'雲量(%)','偏光度(%)','%s'%dic[i],'%s%i'%(dic2[j],k),[[list1[i][0],list2[j][0],list1[i][0],list2[j][1],list1[i][1],list2[j][0],list1[i][1],list2[j][1],'']])
        k+=17
xlsx_file.save(load)