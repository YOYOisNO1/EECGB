    import io, os, sys
    
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    
    
def solve():
        n, m = map(int, input().split())
        exp_n = 0
        exp_sum = []
        while (1 << (exp_n+1)) <= n:
            exp_n += 1
        exp_flag = [0] * ((exp_n * m + 7)//8)
        tmp = 0
        for i in range(1, exp_n+1):
            for j in range(1, m+1):
                coord = i * j - 1
                x, y = coord//8, coord%8
                if exp_flag[x] & (1<<y):
                    continue
                tmp += 1
                exp_flag[x] |= 1 << y
            exp_sum.append(tmp)
    
        ans = 0
        done = [False] * n
        for i in range(1, n+1):
            if done[i-1]:
                continue
    
            done[i-1] = True
            if i == 1:
                ans += 1
                continue
    
            exp_n = 1
            while (i ** (exp_n+1)) <= n:
                exp_n += 1
                done[i ** exp_n -1] = True
            ans += exp_sum[exp_n-1]
        sys.stdout.write(f'{ans}\n')
    
    if __name__ == '__main__':
        solve()