def program521():
        n,m =eval(input())
        arr = [str(input()) for i in range(n)]
        row = [0 for i in range(n)]
        col = [0 for i in range(m)]
         
        for i in range(n):
            for j in range(m):
                if(arr[i][j] == 'S'):
                    row[i] = 1
                    col[j] = 1
                    
        print(n*m - sum(col)*sum(row))