def program2087():
    lst=[]
    for i in range(3):
        lst.append(list(map(int, input().split())))
    lst[0][0] = (lst[0][2]+lst[1][2]+lst[0][1]+lst[2][1]-lst[1][0]-lst[2][0])//2
    lst[2][2] = lst[0][1]+lst[2][1]-lst[0][0]
    lst[1][1] = lst[1][0]+lst[2][0]-lst[2][2]
    print(*i for i in lst)