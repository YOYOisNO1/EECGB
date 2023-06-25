def program2339():
    n, m = list(map(int,input().split()))
    cntr=0
    k = []
    for i in range(n):
    	k.append(input())
    for i in range(n):
        for j in range(m):
            if(k[i][j] == 'W'):
                if(j - 1 >= 0 and k[i][j - 1] == 'P'):
                    cntr += 1
                elif(j + 1 <= m - 1 and k[i][j + 1] == 'P'):
                    cntr += 1
                elif(i - 1 >= 0 and k[i - 1][j] == 'P'):
                    cntr += 1
                elif(i + 1 <= n - 1 and k[i + 1][j] == 'P'):
                    cntr += 1
    print(cntr)