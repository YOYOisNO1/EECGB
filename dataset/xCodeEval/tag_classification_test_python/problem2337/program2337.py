def program2337():
    n,m = map(int, input().split())
    mp = [input() for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if mp[i][j] == 'W':
                if i-1>=0 and mp[i-1][j]=='P' or i+1<n and mp[i+1][j]=='P' \
                or j-1>=0 and mp[i][j-1]=='P' or j+1<m and mp[i][j+1]=='P':
                    ans += 1
    print(ans)