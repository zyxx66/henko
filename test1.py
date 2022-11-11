def pr(*pr):
    if pr.__len__ == 1:
        print('pr len = %d'%1)
    else:
        print('pr len = %d'%pr.__len__())
    for i in pr:
        print(i)


pr([1,2],[3,4],5)