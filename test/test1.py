file = 'C:/Users/zyxx/Desktop/sumup.csv'
data = []
with open(file) as f:
    for i in f:
        data.append(i)

print(data)
start_point_list = []
row_number = 0
for i in range(data.__len__()):
    if 'time' in data[i] :
        start_point_list.append(i)

print(start_point_list)