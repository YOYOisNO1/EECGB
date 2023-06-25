def read_line():
        return [int(i) for i in input().split(' ')]
    
def dp_calc(n, k, d):
        lim = 1000000007
        dist = [[1, 0]]
        for i in range(1, n+1):
            s = [0 , 0]
            for j in range(1, k+1):
                if j > i:
                    break
                if j < d:
                    # distribution does not change
                    s[0] += dist[i-j][0]
                    s[0] %= lim
                    s[1] += dist[i-j][1]
                    s[1] %= lim
                else:
                    # if j >= d then invalid distributions shift to valid
                    s[1] += dist[i-j][0]
                    s[1] %= lim 
                    s[1] += dist[i-j][1]
                    s[1] %= lim
            dist.append(s)
        return dist[n][1]
    
    
    n, k, d = read_line()
    r = dp_calc(n,k,d)
    print(r)