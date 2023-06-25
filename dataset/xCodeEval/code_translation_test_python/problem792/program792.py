def program792():
    n,m=map(int,input().split())
    s=['.'*(m+2)]
    for i in range(n):
        s.append('.'+input()+'.')
    s.append('.'*(m+2))
    r=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i][j]=='W':
                if s[i-1][j] == 'P' or s[i][j-1]=='P' or s[i+1][j]=='P' or s[i][j+1]=='P':
                    r+=1
    print(r) 