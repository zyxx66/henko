folder = 'C://Users/zyxx/Desktop/test_csv/daily_data/'
list =[]
with open(folder+'123.csv') as f:
    for row in f:
        list.append(row)

print(list)

list[0] = list[0].split('\n')[0] + ',6\n'
with open(folder+'123.csv','w') as f:
    for i in range(list.__len__()):
        f.write(list[i])

print(list)