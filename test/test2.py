list = []
for i in range(25):
    list.append('a')

list[0] = list[0]+'123'
print(list)