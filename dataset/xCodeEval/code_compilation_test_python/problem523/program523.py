def program523():
        n,m = eval(input())
        arr = [str(input()) for i in range(n)]
        cnt_row = [0 for i in range(n)]
        cnt_col = [0 for i in range(m)]
         
        for i in range(n):
            for j in range(m):
                if(arr[i][j] == 'S'):
                    cnt_row[i] = 1
                    cnt_col[j] = 1
                    
        print(n*m - sum(cnt_col)*sum(cnt_row))