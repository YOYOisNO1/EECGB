def program332():
    n = input()
    a = [int(i) for i in input().split(' ')]
    # 0 none 1 IT 2 GYM
    d = [[0,0,0] for i in range(n)]
    if a[0]==1:
            d[0][1]=1
    if a[0]==3:
            d[0][1]=1
            d[0][2]=1
    if a[0]==2:
            d[0][2]=1
    
    for i in range(1,n):
            d[i][0]=max(d[i-1])
            d[i][1]=max(d[i-1])
            d[i][2]=max(d[i-1])
            if a[i]==1:
                    d[i][1]=d[i-1][2]+1
            elif a[i]==3:
                    d[i][1]=d[i-1][2]+1
                    d[i][2]=d[i-1][1]+1
            elif a[i]==2:
                    d[i][2]=d[i-1][1]+1
    
    print(n-max(d[n-1]))