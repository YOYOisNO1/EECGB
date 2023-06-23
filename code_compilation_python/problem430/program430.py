def program430():
    a=[[1,1,1],[1,1,1],[1,1,1]]
    b=[]
    ;b.append(list(map(int,input().split())))
    ;b.append(list(map(int,input().split())))
    ;b.append(list(map(int,input().split())))
    for i in range(3):
                       for j in range(3):
                                          if b[i][j]%2==1:
                                                             for k in range(3):
                                                                                if a[k][j] and k!=i:a[k][j]=0
                                                                                else:a[k][j]=1
                                                             for k in range(3):
                                                                                if a[i][k]:a[i][k]=0
                                                                                else:a[i][k]=1
    for i in range(3):print(*a[i])